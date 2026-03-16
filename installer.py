#!/usr/bin/env python3
import os
import sys
import shutil
import platform
import subprocess
import json
import urllib.request
import zipfile

# --- Configuration ---
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
HOME_DIR = os.path.expanduser("~")
BACKUP_ZIP = os.path.join(REPO_DIR, "zsh-backup.zip")
COLOR_SCHEME_JSON = os.path.join(REPO_DIR, "Francisco.json")
OS_TYPE = platform.system()

def log(msg):
    print(f"✨ {msg}")

def error(msg):
    print(f"❌ Error: {msg}")
    sys.exit(1)

def install_fonts():
    log("Checking/Installing Fonts (MesloLGS NF)...")
    fonts = [
        "MesloLGS NF Regular.ttf",
        "MesloLGS NF Bold.ttf",
        "MesloLGS NF Italic.ttf",
        "MesloLGS NF Bold Italic.ttf"
    ]
    base_url = "https://github.com/romkatv/powerlevel10k-media/raw/master/"
    
    if OS_TYPE == "Linux":
        font_dir = os.path.join(HOME_DIR, ".local", "share", "fonts")
    elif OS_TYPE == "Darwin": # macOS
        font_dir = os.path.join(HOME_DIR, "Library", "Fonts")
    else:
        log("Skipping font install (Windows/Other not supported yet).")
        return

    if not os.path.exists(font_dir):
        os.makedirs(font_dir)

    for font in fonts:
        dest = os.path.join(font_dir, font)
        if not os.path.exists(dest):
            log(f"Downloading {font}...")
            try:
                urllib.request.urlretrieve(base_url + font.replace(" ", "%20"), dest)
            except Exception as e:
                print(f"Failed to download {font}: {e}")
    
    if OS_TYPE == "Linux":
        log("Refreshing font cache...")
        subprocess.run(["fc-cache", "-fv"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def restore_dotfiles():
    log("Restoring Dotfiles from zsh-backup.zip...")
    if not os.path.exists(BACKUP_ZIP):
        error(f"Backup zip not found at {BACKUP_ZIP}")

    # Backup existing files
    for f in [".zshrc", ".p10k.zsh", ".oh-my-zsh"]:
        path = os.path.join(HOME_DIR, f)
        if os.path.exists(path):
            backup_path = path + ".bak"
            log(f"Backing up existing {f} to {backup_path}")
            if os.path.isdir(path):
                if os.path.exists(backup_path): shutil.rmtree(backup_path)
                shutil.move(path, backup_path)
            else:
                shutil.move(path, backup_path)

    # Extract zip
    try:
        with zipfile.ZipFile(BACKUP_ZIP, 'r') as zip_ref:
            # Check root folder structure
            # If the zip has a root folder like 'zsh-backup/', we need to handle it.
            # Assuming zip structure is zsh-backup/{.zshrc, .p10k.zsh, .oh-my-zsh/}
            
            temp_extract = os.path.join(HOME_DIR, "temp_zsh_extract")
            if os.path.exists(temp_extract): shutil.rmtree(temp_extract)
            zip_ref.extractall(temp_extract)
            
            # Find the inner content
            extracted_root = os.path.join(temp_extract, "zsh-backup")
            if not os.path.isdir(extracted_root):
                # Maybe flat structure?
                extracted_root = temp_extract

            # Move files to HOME
            items = os.listdir(extracted_root)
            for item in items:
                src = os.path.join(extracted_root, item)
                dst = os.path.join(HOME_DIR, item)
                if item in [".zshrc", ".p10k.zsh", ".oh-my-zsh"]:
                     if os.path.exists(dst): 
                         if os.path.isdir(dst): shutil.rmtree(dst)
                         else: os.remove(dst)
                     shutil.move(src, dst)
            
            # Cleanup
            shutil.rmtree(temp_extract)
            log("Dotfiles restored successfully.")

    except Exception as e:
        error(f"Failed to extract zip: {e}")

def install_colorls():
    log("Installing colorls gem...")
    try:
        # Check if colorls is already installed
        subprocess.check_call(["gem", "list", "-i", "colorls"], stdout=subprocess.DEVNULL)
        log("colorls is already installed.")
    except subprocess.CalledProcessError:
        try:
            # Try user install first to avoid permission issues
            subprocess.check_call(["gem", "install", "colorls", "--user-install"])
        except subprocess.CalledProcessError:
            log("User install failed, trying with sudo...")
            try:
                subprocess.check_call(["sudo", "gem", "install", "colorls"])
            except subprocess.CalledProcessError:
                print("⚠️  Could not install colorls. Please run 'sudo gem install colorls' manually.")

def hex_color(r, g, b):
    # Convert 0-1 float to 0-255 int hex
    return "#{:02x}{:02x}{:02x}".format(int(r*255), int(g*255), int(b*255))

def configure_terminator_linux():
    log("Configuring Terminator (Linux)...")
    config_dir = os.path.join(HOME_DIR, ".config", "terminator")
    config_file = os.path.join(config_dir, "config")
    
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    try:
        with open(COLOR_SCHEME_JSON, 'r') as f:
            data = json.load(f)
        
        # Mapping logic (simplified from analysis)
        # We need 16 colors for the palette
        palette = []
        for i in range(16):
            key = f"Ansi {i} Color"
            # Try specific variants if needed, but standard keys work best usually.
            # Fallback to (Dark) if present as per user preference for dark theme.
            key_dark = f"{key} (Dark)"
            if key_dark in data:
                c = data[key_dark]
            elif key in data:
                c = data[key]
            else:
                c = {"Red Component": 0, "Green Component": 0, "Blue Component": 0} # Fallback black
            
            palette.append(hex_color(c.get("Red Component", 0), c.get("Green Component", 0), c.get("Blue Component", 0)))
        
        palette_str = ":".join(palette)
        
        # Background/Foreground
        bg_data = data.get("Background Color (Dark)", data.get("Background Color", {}))
        fg_data = data.get("Foreground Color (Dark)", data.get("Foreground Color", {}))
        cursor_data = data.get("Cursor Color", {})
        
        bg_hex = hex_color(bg_data.get("Red Component", 0), bg_data.get("Green Component", 0), bg_data.get("Blue Component", 0))
        fg_hex = hex_color(fg_data.get("Red Component", 0), fg_data.get("Green Component", 0), fg_data.get("Blue Component", 0))
        cursor_hex = hex_color(cursor_data.get("Red Component", 0), cursor_data.get("Green Component", 0), cursor_data.get("Blue Component", 0))

        config_content = f"""[global_config]
  title_transmit_bg_color = "{bg_hex}"
[keybindings]
[profiles]
  [[default]]
    background_color = "{bg_hex}"
    cursor_color = "{cursor_hex}"
    font = MesloLGS NF 12
    foreground_color = "{fg_hex}"
    palette = "{palette_str}"
    show_titlebar = False
    use_system_font = False
    command = /usr/bin/zsh
"""
        with open(config_file, 'w') as f:
            f.write(config_content)
        log(f"Terminator config written to {config_file}")

    except Exception as e:
        print(f"⚠️  Failed to configure Terminator: {e}")

def configure_iterm_mac():
    log("Configuring iTerm2 (macOS)...")
    log(f"Opening '{COLOR_SCHEME_JSON}' - please verify and import it if iTerm2 prompts you.")
    try:
        subprocess.run(["open", COLOR_SCHEME_JSON])
    except:
        pass
    print("ℹ️  Manual Step: Open iTerm2 > Preferences > Profiles > Colors > Color Presets > Import...")
    print(f"   Select the file: {COLOR_SCHEME_JSON}")
    print("   Also set Font to 'MesloLGS NF' in Text settings.")

def main():
    log(f"Starting Installer on {OS_TYPE}...")
    
    install_fonts()
    restore_dotfiles()
    install_colorls()
    
    if OS_TYPE == "Linux":
        configure_terminator_linux()
    elif OS_TYPE == "Darwin":
        configure_iterm_mac()
    
    log("Installation Complete! 🚀")
    print("\nPlease restart your terminal to see the changes.")

if __name__ == "__main__":
    main()

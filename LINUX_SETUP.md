# Linux (Lubuntu) Setup Guide

This guide details how the macOS configuration was adapted for Linux (Lubuntu) using Terminator.

## 1. Prerequisites
Install the following packages:
```bash
sudo apt update
sudo apt install -y terminator zsh git curl wget ruby-full build-essential
```

## 2. Fonts
Download and install the MesloLGS NF fonts required for Powerlevel10k:
```bash
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts
wget -q -O "MesloLGS NF Regular.ttf" "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf"
wget -q -O "MesloLGS NF Bold.ttf" "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf"
wget -q -O "MesloLGS NF Italic.ttf" "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf"
wget -q -O "MesloLGS NF Bold Italic.ttf" "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf"
fc-cache -fv
```

## 3. Zsh & Oh My Zsh
1.  **Change Default Shell:**
    ```bash
    chsh -s $(which zsh)
    ```
2.  **Restore Configuration:**
    Extract the `zsh-backup.zip` file:
    ```bash
    unzip zsh-backup.zip
    cp zsh-backup/.zshrc ~/.zshrc
    cp zsh-backup/.p10k.zsh ~/.p10k.zsh
    rm -rf ~/.oh-my-zsh
    mv zsh-backup/.oh-my-zsh ~/.oh-my-zsh
    ```

## 4. Terminator Configuration
The iTerm2 color scheme (`Francisco.json`) was converted to Terminator format.
Copy the content below to `~/.config/terminator/config`:

```ini
[global_config]
  title_transmit_bg_color = "#101216"
[keybindings]
[profiles]
  [[default]]
    background_color = "#101216"
    cursor_color = "#C9D9D1"
    font = MesloLGS NF 12
    foreground_color = "#8B9E94"
    palette = "#000000:#F76681:#56D364:#E3B341:#6CA4F8:#DB61A2:#2B7489:#FFFFFF:#4D4D4D:#F76681:#56D364:#E3B341:#6CA4F8:#DB61A2:#2B7489:#FFFFFF"
    show_titlebar = False
    use_system_font = False
```

## 5. Extra Tools
Install `colorls` gem:
```bash
sudo gem install colorls
```

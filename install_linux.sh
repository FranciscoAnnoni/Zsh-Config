#!/bin/bash
set -e

echo "🐧 Starting Linux Setup..."

# Update and Install Dependencies
echo "📦 Installing dependencies..."
sudo apt update
sudo apt install -y git zsh terminator python3 ruby-full build-essential curl wget unzip

# Check if Zsh is installed
if ! command -v zsh &> /dev/null; then
    echo "❌ Zsh failed to install. Please install it manually."
    exit 1
fi

# Clone Repo if not present
REPO_DIR="$HOME/proyectos/Zsh-Config"
if [ ! -d "$REPO_DIR" ]; then
    echo "📥 Cloning Zsh-Config repository..."
    mkdir -p "$HOME/proyectos"
    git clone https://github.com/FranciscoAnnoni/Zsh-Config.git "$REPO_DIR"
else
    echo "✅ Repository already exists at $REPO_DIR"
    cd "$REPO_DIR" && git pull
fi

# Change default shell to Zsh
if [ "$SHELL" != "$(which zsh)" ]; then
    echo "🐚 Changing default shell to Zsh..."
    chsh -s "$(which zsh)"
fi

# Run Python Installer
echo "🚀 Launching configuration script..."
python3 "$REPO_DIR/installer.py"

echo "🎉 Linux setup complete! Please restart your terminal."

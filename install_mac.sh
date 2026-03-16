#!/bin/bash
set -e

echo "🍎 Starting macOS Setup..."

# Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo "🍺 Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅ Homebrew is already installed."
    brew update
fi

# Install Dependencies
echo "📦 Installing dependencies via Homebrew..."
brew install git python3 wget curl ruby zsh
brew install --cask iterm2

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

echo "🎉 macOS setup complete! Please restart iTerm2."

#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
else
    # Install Homebrew (if not already installed)
    if ! command -v brew &>/dev/null; then
        echo "Homebrew is not installed. Installing..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    # Install Python
    echo "Python is not installed. Installing..."
    brew install python@3.12
fi

# Install required Python packages
echo "Installing required Python packages..."
python3 -m pip install PySide6 numpy matplotlib argparse tqdm

# Run Python script
python3 ui.py

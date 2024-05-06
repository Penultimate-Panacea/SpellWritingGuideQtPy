#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
else
    # Install Python
    echo "Python is not installed. Installing..."
    
    # Check package manager and install Python
    if command -v apt-get &>/dev/null; then
        sudo apt-get update
        sudo apt-get install python3
    elif command -v yum &>/dev/null; then
        sudo yum install python3
    else
        echo "Unsupported package manager. Please install Python manually."
        exit 1
    fi
fi

# Install needed packages
echo Installing required Python packages...
python -m pip install pyside numpy matplotlib argparse math os tqdm
# Run Python script
python3 ui.py

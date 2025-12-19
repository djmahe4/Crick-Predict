#!/bin/bash
# ============================================================================
# Crick-Predict Installation Script for Linux
# ============================================================================
# This script installs all dependencies for the Crick-Predict application
# including Python packages and Playwright browsers.
#
# Prerequisites:
#   - Python 3.8 or higher must be installed
#   - pip must be available
#
# Usage: Make executable and run:
#        chmod +x install_linux.sh
#        ./install_linux.sh
# ============================================================================

echo "============================================================================"
echo "Crick-Predict Installation Script for Linux"
echo "============================================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  Fedora/RHEL:   sudo dnf install python3 python3-pip"
    echo "  Arch:          sudo pacman -S python python-pip"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "Python detected: $PYTHON_VERSION"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip is not installed"
    echo "Please install pip:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-pip"
    echo "  Fedora/RHEL:   sudo dnf install python3-pip"
    echo "  Arch:          sudo pacman -S python-pip"
    exit 1
fi

PIP_VERSION=$(pip3 --version)
echo "pip detected: $PIP_VERSION"
echo ""

echo "============================================================================"
echo "Step 1: Upgrading pip, setuptools, and wheel"
echo "============================================================================"
python3 -m pip install --upgrade pip setuptools wheel --user
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to upgrade pip"
    exit 1
fi
echo ""

echo "============================================================================"
echo "Step 2: Installing Python dependencies from requirements.txt"
echo "============================================================================"
pip3 install -r requirements.txt --user
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install Python dependencies"
    exit 1
fi
echo ""

echo "============================================================================"
echo "Step 3: Installing system dependencies for Playwright"
echo "============================================================================"
echo "Note: This may require sudo password for installing system dependencies"
playwright install-deps chromium
echo ""

echo "============================================================================"
echo "Step 4: Installing Playwright browsers (Chromium)"
echo "============================================================================"
echo "This may take several minutes depending on your internet connection..."
playwright install chromium
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install Playwright browsers"
    echo "You can try installing manually with: playwright install chromium"
    exit 1
fi
echo ""

echo "============================================================================"
echo "Step 5: Verifying installation"
echo "============================================================================"
python3 -c "import streamlit; import playwright; import pandas; import matplotlib; print('All core packages imported successfully!')"
if [ $? -ne 0 ]; then
    echo "WARNING: Some packages may not have been installed correctly"
    echo "Please check the error messages above"
    exit 1
fi
echo ""

echo "============================================================================"
echo "Step 6: Running functionality tests"
echo "============================================================================"
python3 test_functionality.py
if [ $? -ne 0 ]; then
    echo "WARNING: Some functionality tests failed"
    echo "The application may still work, but please check the error messages"
fi
echo ""

echo "============================================================================"
echo "Installation completed successfully!"
echo "============================================================================"
echo ""
echo "To run the application:"
echo "  1. Open terminal in this directory"
echo "  2. Run: streamlit run app.py"
echo ""
echo "Or run: ./run_linux.sh"
echo "============================================================================"

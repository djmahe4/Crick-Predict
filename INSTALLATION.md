# Installation Guide for Crick-Predict

This guide provides detailed instructions for installing and running the Crick-Predict application on different operating systems.

## Table of Contents
- [Windows Installation (Recommended for Windows Users)](#windows-installation)
- [Linux Installation](#linux-installation)
- [macOS Installation](#macos-installation)
- [Manual Installation (All Platforms)](#manual-installation)
- [Troubleshooting](#troubleshooting)

---

## Windows Installation

### Prerequisites
- **Python 3.8 or higher** - [Download from python.org](https://www.python.org/downloads/)
  - ⚠️ **IMPORTANT**: During installation, check the box "Add Python to PATH"
- **Windows 10 or higher** (Windows 11 recommended)
- **Active Internet Connection** for downloading dependencies

### Option 1: Automated Installation (Recommended)

#### Using Batch File (.bat)
1. Open File Explorer and navigate to the Crick-Predict folder
2. Double-click `install_windows.bat`
3. Wait for the installation to complete (may take 5-10 minutes)
4. Once complete, double-click `run_windows.bat` to start the application

#### Using PowerShell (.ps1)
1. Open File Explorer and navigate to the Crick-Predict folder
2. Right-click `install_windows.ps1` and select "Run with PowerShell"
   - If you get a security warning, you may need to enable script execution:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```
3. Wait for the installation to complete (may take 5-10 minutes)
4. Run the application:
   ```powershell
   streamlit run app.py
   ```

### Option 2: Command Prompt Installation
1. Open Command Prompt (search for "cmd" in Start menu)
2. Navigate to the project directory:
   ```cmd
   cd path\to\Crick-Predict
   ```
3. Run the installation script:
   ```cmd
   install_windows.bat
   ```
4. Run the application:
   ```cmd
   run_windows.bat
   ```

---

## Linux Installation

### Prerequisites
- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Active Internet Connection**

### Distribution-Specific Python Installation

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

#### Fedora/RHEL/CentOS
```bash
sudo dnf install python3 python3-pip
```

#### Arch Linux
```bash
sudo pacman -S python python-pip
```

### Automated Installation

1. Open Terminal
2. Navigate to the project directory:
   ```bash
   cd /path/to/Crick-Predict
   ```
3. Make the installation script executable:
   ```bash
   chmod +x install_linux.sh
   ```
4. Run the installation script:
   ```bash
   ./install_linux.sh
   ```
5. Run the application:
   ```bash
   ./run_linux.sh
   ```
   Or:
   ```bash
   streamlit run app.py
   ```

---

## macOS Installation

### Prerequisites
- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Active Internet Connection**

### Installing Python on macOS

#### Option 1: Using Homebrew (Recommended)
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3
```

#### Option 2: Official Python Installer
Download from [python.org/downloads/macos](https://www.python.org/downloads/macos/)

### Automated Installation

1. Open Terminal
2. Navigate to the project directory:
   ```bash
   cd /path/to/Crick-Predict
   ```
3. Make the installation script executable:
   ```bash
   chmod +x install_macos.sh
   ```
4. Run the installation script:
   ```bash
   ./install_macos.sh
   ```
5. Run the application:
   ```bash
   ./run_macos.sh
   ```
   Or:
   ```bash
   streamlit run app.py
   ```

---

## Manual Installation (All Platforms)

If the automated scripts don't work, follow these manual steps:

### Step 1: Verify Python Installation
```bash
# Check Python version (should be 3.8 or higher)
python --version
# or on Linux/macOS
python3 --version
```

### Step 2: Install Python Dependencies
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### Step 3: Install Playwright Browsers
```bash
# Install Chromium browser for Playwright
playwright install chromium

# On Linux, you may also need system dependencies
playwright install-deps chromium
```

### Step 4: Verify Installation
```bash
python -c "import streamlit; import playwright; import pandas; print('Installation successful!')"
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

---

## Troubleshooting

### Common Issues

#### 1. "Python is not recognized as an internal or external command" (Windows)
**Solution**: Python is not in your system PATH
- Reinstall Python and check "Add Python to PATH" during installation
- Or manually add Python to PATH:
  1. Search for "Environment Variables" in Start menu
  2. Click "Environment Variables"
  3. Under "System variables", find and edit "Path"
  4. Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python3X`

#### 2. "Permission denied" error (Linux/macOS)
**Solution**: Make scripts executable
```bash
chmod +x install_linux.sh run_linux.sh
# or
chmod +x install_macos.sh run_macos.sh
```

#### 3. Playwright installation fails
**Solution**: 
- Check your internet connection
- Try installing manually:
  ```bash
  playwright install chromium
  ```
- On Linux, install system dependencies:
  ```bash
  playwright install-deps chromium
  ```

#### 4. "ModuleNotFoundError" when running the app
**Solution**: Dependencies not installed properly
```bash
pip install -r requirements.txt --force-reinstall
```

#### 5. Browser fails to launch
**Solution**: 
- Ensure Playwright browsers are installed:
  ```bash
  playwright install chromium
  ```
- Check if antivirus is blocking browser execution
- On Windows, check Windows Defender settings

#### 6. Streamlit port already in use
**Solution**: Specify a different port
```bash
streamlit run app.py --server.port 8502
```

### Getting Help

If you encounter issues not covered here:
1. Check the error message carefully
2. Ensure all prerequisites are installed
3. Try running the manual installation steps
4. Check GitHub Issues for similar problems
5. Create a new issue with:
   - Your operating system and version
   - Python version (`python --version`)
   - Complete error message
   - Steps you've already tried

---

## Post-Installation

### Accessing the Application

Once running, the application will automatically open in your default web browser at:
```
http://localhost:8501
```

If it doesn't open automatically, manually navigate to this URL in your browser.

### Application Features

The application includes four main pages:
1. **App** 🏏 - Main prediction interface for upcoming matches
2. **Player Stats** 📊 - View detailed player statistics
3. **Learn** 🎓 - Analyze past matches for learning
4. **Data** ℹ️ - Export and analyze match data

### Stopping the Application

- **Windows**: Press `Ctrl+C` in the Command Prompt window
- **Linux/macOS**: Press `Ctrl+C` in the Terminal window

---

## System Requirements

### Minimum Requirements
- **OS**: Windows 10, Ubuntu 20.04, macOS 10.15 or newer
- **CPU**: Dual-core processor
- **RAM**: 4 GB
- **Disk Space**: 2 GB free space
- **Internet**: Broadband connection for scraping data

### Recommended Requirements
- **OS**: Windows 11, Ubuntu 22.04, macOS 12 or newer
- **CPU**: Quad-core processor
- **RAM**: 8 GB or more
- **Disk Space**: 5 GB free space
- **Internet**: High-speed broadband connection

---

## Running Tests

### Automated Testing (CI/CD)

The repository includes GitHub Actions workflows that automatically test the application on every code change:

- **Quick Check**: Runs on every push/PR to verify basic functionality
- **Full Test Suite**: Comprehensive tests across multiple Python versions
- **Security Scan**: Checks for vulnerabilities in dependencies
- **Integration Test**: Tests the full installation process

View test results in the "Actions" tab on GitHub.

### Local Testing

You can run the test suite locally:

```bash
# Run the functionality tests
python test_functionality.py

# Or on Linux/macOS
python3 test_functionality.py
```

The test script checks:
- Python file syntax validation
- Core package imports (Streamlit, Playwright, Pandas, etc.)
- Custom module imports
- Cricket workflow functionality
- Browser automation capabilities

---

## Notes

- First-time scraping may be slower as the browser initializes
- The application requires an active internet connection to fetch cricket data
- Browser automation may be blocked by some corporate firewalls
- Keep your Python and dependencies updated for best performance
- All installation scripts include functionality tests that run automatically
- CI/CD workflows ensure code quality and functionality on every change

---

## License

See LICENSE file for details.

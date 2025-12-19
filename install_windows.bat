@echo off
REM ============================================================================
REM Crick-Predict Installation Script for Windows
REM ============================================================================
REM This script installs all dependencies for the Crick-Predict application
REM including Python packages and Playwright browsers.
REM
REM Prerequisites:
REM   - Python 3.8 or higher must be installed
REM   - pip must be available
REM
REM Usage: Double-click this file or run from Command Prompt:
REM        install_windows.bat
REM ============================================================================

echo ============================================================================
echo Crick-Predict Installation Script for Windows
echo ============================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python detected:
python --version
echo.

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip is not installed or not in PATH
    echo Please install pip or reinstall Python with pip
    pause
    exit /b 1
)

echo pip detected:
pip --version
echo.

echo ============================================================================
echo Step 1: Upgrading pip, setuptools, and wheel
echo ============================================================================
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip
    pause
    exit /b 1
)
echo.

echo ============================================================================
echo Step 2: Installing Python dependencies from requirements.txt
echo ============================================================================
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies
    pause
    exit /b 1
)
echo.

echo ============================================================================
echo Step 3: Installing Playwright browsers (Chromium)
echo ============================================================================
echo This may take several minutes depending on your internet connection...
playwright install chromium
if errorlevel 1 (
    echo ERROR: Failed to install Playwright browsers
    echo You can try installing manually with: playwright install chromium
    pause
    exit /b 1
)
echo.

echo ============================================================================
echo Step 4: Verifying installation
echo ============================================================================
python -c "import streamlit; import playwright; import pandas; import matplotlib; print('All core packages imported successfully!')"
if errorlevel 1 (
    echo WARNING: Some packages may not have been installed correctly
    echo Please check the error messages above
    pause
    exit /b 1
)
echo.

echo ============================================================================
echo Step 5: Running functionality tests
echo ============================================================================
python test_functionality.py
if errorlevel 1 (
    echo WARNING: Some functionality tests failed
    echo The application may still work, but please check the error messages
)
echo.

echo ============================================================================
echo Installation completed successfully!
echo ============================================================================
echo.
echo To run the application:
echo   1. Open Command Prompt or PowerShell in this directory
echo   2. Run: streamlit run app.py
echo.
echo Or simply double-click the run_windows.bat file
echo ============================================================================
pause

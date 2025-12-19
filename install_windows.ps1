# ============================================================================
# Crick-Predict Installation Script for Windows (PowerShell)
# ============================================================================
# This script installs all dependencies for the Crick-Predict application
# including Python packages and Playwright browsers.
#
# Prerequisites:
#   - Python 3.8 or higher must be installed
#   - pip must be available
#
# Usage: Right-click and "Run with PowerShell" or run from PowerShell:
#        .\install_windows.ps1
# ============================================================================

Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Crick-Predict Installation Script for Windows (PowerShell)" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python detected: $pythonVersion" -ForegroundColor Green
    Write-Host ""
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8 or higher from https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if pip is installed
try {
    $pipVersion = pip --version 2>&1
    Write-Host "pip detected: $pipVersion" -ForegroundColor Green
    Write-Host ""
} catch {
    Write-Host "ERROR: pip is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install pip or reinstall Python with pip" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Step 1: Upgrading pip, setuptools, and wheel" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
python -m pip install --upgrade pip setuptools wheel
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to upgrade pip" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Step 2: Installing Python dependencies from requirements.txt" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install Python dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Step 3: Installing Playwright browsers (Chromium)" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "This may take several minutes depending on your internet connection..." -ForegroundColor Yellow
playwright install chromium
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install Playwright browsers" -ForegroundColor Red
    Write-Host "You can try installing manually with: playwright install chromium" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Step 4: Verifying installation" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
python -c "import streamlit; import playwright; import pandas; import matplotlib; print('All core packages imported successfully!')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "WARNING: Some packages may not have been installed correctly" -ForegroundColor Yellow
    Write-Host "Please check the error messages above" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Step 5: Running functionality tests" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
python test_functionality.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "WARNING: Some functionality tests failed" -ForegroundColor Yellow
    Write-Host "The application may still work, but please check the error messages" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "============================================================================" -ForegroundColor Green
Write-Host "Installation completed successfully!" -ForegroundColor Green
Write-Host "============================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Cyan
Write-Host "  1. Open Command Prompt or PowerShell in this directory" -ForegroundColor White
Write-Host "  2. Run: streamlit run app.py" -ForegroundColor White
Write-Host ""
Write-Host "Or simply double-click the run_windows.bat file" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
Read-Host "Press Enter to exit"

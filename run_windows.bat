@echo off
REM ============================================================================
REM Crick-Predict Run Script for Windows
REM ============================================================================
REM This script runs the Streamlit application
REM
REM Prerequisites:
REM   - Dependencies must be installed (run install_windows.bat first)
REM
REM Usage: Double-click this file or run from Command Prompt:
REM        run_windows.bat
REM ============================================================================

echo ============================================================================
echo Starting Crick-Predict Application
echo ============================================================================
echo.
echo The application will open in your default web browser.
echo To stop the application, press Ctrl+C in this window.
echo.
echo ============================================================================
echo.

REM Check if streamlit is installed
streamlit --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Streamlit is not installed
    echo Please run install_windows.bat first
    pause
    exit /b 1
)

REM Run the Streamlit app
streamlit run app.py

pause

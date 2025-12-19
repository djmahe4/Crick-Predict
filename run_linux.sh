#!/bin/bash
# ============================================================================
# Crick-Predict Run Script for Linux
# ============================================================================
# This script runs the Streamlit application
#
# Prerequisites:
#   - Dependencies must be installed (run install_linux.sh first)
#
# Usage: Make executable and run:
#        chmod +x run_linux.sh
#        ./run_linux.sh
# ============================================================================

echo "============================================================================"
echo "Starting Crick-Predict Application"
echo "============================================================================"
echo ""
echo "The application will open in your default web browser."
echo "To stop the application, press Ctrl+C in this terminal."
echo ""
echo "============================================================================"
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "ERROR: Streamlit is not installed"
    echo "Please run install_linux.sh first"
    exit 1
fi

# Run the Streamlit app
streamlit run app.py

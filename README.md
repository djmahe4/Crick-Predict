# Crick-Predict 🏏

A cricket prediction application using numerology and biorhythm analysis to predict player performance in upcoming matches.

## 🌟 Features

- **Match Prediction**: Analyze upcoming cricket matches using numerology and biorhythm calculations
- **Player Statistics**: View detailed statistics for any cricket player including:
  - Basic information (name, country, playing role)
  - Playing style (batting, bowling)
  - Match history
  - Date of birth information
- **Team Analysis**: Get team statistics and information
- **Match History Learning**: Analyze past matches to improve prediction accuracy
- **Data Export**: Export prediction data for further analysis
- **Live Browser Scraping**: Uses Playwright for reliable data fetching from ESPN Cricinfo

## 🚀 Quick Start

### For Windows Users (Recommended)
1. Download or clone this repository
2. Double-click `install_windows.bat` to install all dependencies
3. Double-click `run_windows.bat` to start the application

### For Linux/macOS Users
1. Clone this repository
2. Run the installation script:
   ```bash
   chmod +x install_linux.sh  # or install_macos.sh
   ./install_linux.sh         # or ./install_macos.sh
   ```
3. Run the application:
   ```bash
   ./run_linux.sh  # or ./run_macos.sh
   ```

## 📋 Requirements

- Python 3.8 or higher
- Internet connection for fetching match data
- 2 GB free disk space
- Modern web browser (Chrome/Chromium)

## 📖 Detailed Installation

For detailed installation instructions for your operating system, see [INSTALLATION.md](INSTALLATION.md)

## 🎯 How to Use

1. **Select a Match**: Choose from upcoming matches in the dropdown
2. **Run Analysis**: Click "Start" to analyze players using numerology
3. **View Results**: See biorhythm charts and predictions for each player
4. **Export Data**: Go to the "Data" tab to export your predictions
5. **Check Player Stats**: Use the "Player Stats" tab to view detailed player information
6. **Learn from History**: Use the "Learn" tab to analyze past matches

### Understanding Predictions
If you don't know how to interpret predictions, try analyzing previous matches in the "Learn" tab to see how the predictions aligned with actual performance.

## 🌐 Online Version

Try the hosted version: [CLICK HERE](https://crick-predict.streamlit.app/)

## 🛠️ Technology Stack

- **Streamlit**: Web application framework
- **Playwright**: Browser automation for data scraping
- **BeautifulSoup4**: HTML parsing
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Biorhythm chart visualization
- **Python**: Core programming language

## 📁 Project Structure

```
Crick-Predict/
├── app.py                      # Main Streamlit application
├── cricket_workflow.py         # Data scraping and workflow module (NEW)
├── numerology.py               # Numerology and biorhythm calculations
├── debug.py                    # Past match analysis page
├── test.py                     # Compatibility wrapper
├── test_functionality.py       # Automated test suite (NEW)
├── requirements.txt            # Python dependencies
├── install_windows.bat         # Windows installer (Batch) (NEW)
├── install_windows.ps1         # Windows installer (PowerShell) (NEW)
├── run_windows.bat             # Windows run script (NEW)
├── install_linux.sh            # Linux installer (NEW)
├── run_linux.sh                # Linux run script (NEW)
├── install_macos.sh            # macOS installer (NEW)
├── run_macos.sh                # macOS run script (NEW)
├── .github/workflows/          # CI/CD workflows (NEW)
│   ├── test.yml                # Comprehensive test suite
│   └── quick-check.yml         # Quick validation on commits
├── INSTALLATION.md             # Detailed installation guide (NEW)
├── WORKFLOW_GUIDE.md           # Architecture and workflow docs (NEW)
├── .gitignore                  # Git ignore patterns
└── README.md                   # This file
```

For detailed workflow and architecture information, see [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)

## ✅ Testing

The project includes comprehensive testing:

### Automated CI/CD
- **GitHub Actions workflows** run on every code change
- Tests across Python 3.8, 3.9, 3.10, 3.11, and 3.12
- Code quality checks with flake8 and pylint
- Security scanning with safety and bandit
- Integration tests to verify full installation

### Local Testing
Run the test suite locally:
```bash
python test_functionality.py
```

Tests verify:
- ✓ Python file syntax
- ✓ Core package imports
- ✓ Custom module functionality
- ✓ Browser automation
- ✓ Cricket workflow operations

## 🔧 Troubleshooting

Common issues and solutions:

1. **"Python not found"**: Make sure Python is installed and added to PATH
2. **"Module not found"**: Run the installation script again
3. **Browser fails to launch**: Reinstall Playwright browsers with `playwright install chromium`
4. **Port already in use**: Run with a different port: `streamlit run app.py --server.port 8502`

For more troubleshooting help, see [INSTALLATION.md](INSTALLATION.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This application uses numerology and biorhythm analysis for entertainment purposes. Cricket match outcomes depend on many factors including form, fitness, pitch conditions, weather, and team strategy. Use predictions responsibly and for entertainment only.

## 📞 Support

If you encounter any issues:
1. Check the [INSTALLATION.md](INSTALLATION.md) guide
2. Review the troubleshooting section above
3. Create an issue on GitHub with detailed information about your problem

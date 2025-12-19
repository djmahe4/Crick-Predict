# Getting Started with Crick-Predict

Welcome! This guide will help you get started with the newly refactored Crick-Predict application.

## 🎯 What's New?

The application has been significantly upgraded with:
- ✅ **Browser-based scraping** using Playwright (more reliable!)
- ✅ **Separated workflow** for better code organization
- ✅ **Player statistics** viewing feature
- ✅ **Installation scripts** for Windows, Linux, and macOS
- ✅ **Automated testing** on every code change
- ✅ **Comprehensive documentation**

## 🚀 Quick Start

### For Windows Users (Recommended)

1. **Download/Clone the repository**
2. **Run the installer**:
   - Double-click `install_windows.bat`
   - Or right-click `install_windows.ps1` → "Run with PowerShell"
3. **Wait for installation** (5-10 minutes)
4. **Start the app**:
   - Double-click `run_windows.bat`
   - Or run `streamlit run app.py` in Command Prompt

### For Linux Users

```bash
# Make executable and install
chmod +x install_linux.sh
./install_linux.sh

# Run the application
./run_linux.sh
```

### For macOS Users

```bash
# Make executable and install
chmod +x install_macos.sh
./install_macos.sh

# Run the application
./run_macos.sh
```

## 📱 Using the Application

Once the application starts, you'll see it in your web browser at `http://localhost:8501`

### Main Features

#### 1. App (🏏) - Predict Upcoming Matches
- Select an upcoming cricket match
- Choose "numerology" analysis
- Click "Start" to analyze
- View biorhythm charts for each player
- See predictions for match day

#### 2. Player Stats (📊) - NEW!
- Enter a player's ESPN Cricinfo URL
- Click "Get Player Stats"
- View:
  - Player name and country
  - Playing role (Batsman, Bowler, etc.)
  - Batting and bowling styles
  - Date of birth
  - Recent match statistics

#### 3. Learn (🎓) - Analyze Past Matches
- Select a completed match
- Run analysis to see predictions vs actual
- Learn from historical data
- View MVP (Most Valuable Player) lists

#### 4. Data (ℹ️) - Export Predictions
- Download your predictions as CSV
- Includes biorhythm values
- Compare with Dream11 top picks

## 🔍 Key Improvements Explained

### 1. Browser-Based Scraping

**Before**: Used HTTP requests that could fail with JavaScript-heavy sites
**Now**: Uses a real browser (Chromium) via Playwright

**Benefits**:
- More reliable data fetching
- Handles dynamic content
- Less likely to be blocked
- Better error handling

### 2. Separated Workflow

**Before**: Everything mixed in a few files
**Now**: Clean modular architecture

```
app.py           → User Interface
numerology.py    → Calculations
cricket_workflow.py → Data Fetching (NEW!)
```

**Benefits**:
- Easier to maintain
- Easier to test
- Easier to add features
- Better code organization

### 3. Installation Scripts

**Before**: Manual pip install, manual browser setup
**Now**: One-click installation

**Benefits**:
- Automated setup
- Tests run automatically
- OS-specific optimizations
- Clear error messages

### 4. Automated Testing

**Before**: No automated tests
**Now**: Comprehensive CI/CD

**Benefits**:
- Catches bugs early
- Tests on multiple Python versions
- Security scanning
- Quality assurance

## 📚 Documentation

We've created comprehensive documentation:

- **README.md** - Overview and quick start
- **INSTALLATION.md** - Detailed installation guide
- **WORKFLOW_GUIDE.md** - Architecture and development guide
- **CHANGES.md** - Summary of all changes
- **GETTING_STARTED.md** - This file

## 🧪 Testing

### Run Tests Locally

```bash
python test_functionality.py
```

This will verify:
- ✓ All Python files have valid syntax
- ✓ All packages are installed
- ✓ All modules can be imported
- ✓ Browser automation works
- ✓ Cricket workflow functions work

### Automated Testing

Every time you push code to GitHub:
- Quick syntax check runs (~5 min)
- Full test suite runs on PRs (~15 min)
- Tests on Python 3.8, 3.9, 3.10, 3.11, 3.12
- Code quality checks
- Security scanning

View results in the "Actions" tab on GitHub.

## 🎓 Learning Resources

### For Users

1. **First time?** Start with the "Learn" tab to see past predictions
2. **Understanding predictions**: Higher biorhythm values = better predicted performance
3. **Best practice**: Compare predictions with actual Dream11 points after matches

### For Developers

1. **Architecture**: Read `WORKFLOW_GUIDE.md`
2. **Adding features**: Check "For Developers" section in `WORKFLOW_GUIDE.md`
3. **Contributing**: See Contributing section in `README.md`

## 🛠️ Troubleshooting

### Common Issues

#### "Python not found"
**Solution**: Install Python 3.8+ from python.org, check "Add to PATH"

#### "Streamlit not installed"
**Solution**: Run the installation script again

#### "Browser fails to launch"
**Solution**: 
```bash
playwright install chromium
# On Linux also run:
playwright install-deps chromium
```

#### Port already in use
**Solution**: 
```bash
streamlit run app.py --server.port 8502
```

### Getting More Help

1. Check `INSTALLATION.md` troubleshooting section
2. Run test suite: `python test_functionality.py`
3. Check GitHub Issues
4. Create new issue with:
   - Your OS and version
   - Python version
   - Complete error message
   - Steps to reproduce

## 📊 Example Usage

### Predicting a Match

```python
# This is done automatically in the UI, but here's what happens:

# 1. Select match (UI does this)
match_url = "https://www.espncricinfo.com/series/.../live-cricket-score"

# 2. Get players (cricket_workflow does this)
from cricket_workflow import match11
players, match_date = match11(match_url)

# 3. Run analysis (numerology does this)
from numerology import main
main(match_url)

# 4. View results (Streamlit shows this)
```

### Getting Player Stats

```python
from cricket_workflow import get_player_stats

# Get stats for a player
player_url = "https://www.espncricinfo.com/cricketers/player-name-12345"
stats = get_player_stats(player_url)

print(f"Player: {stats['name']}")
print(f"Country: {stats['country']}")
print(f"Role: {stats['playingRole']}")
print(f"Batting: {stats['battingStyle']}")
print(f"Bowling: {stats['bowlingStyle']}")
```

## 🎯 Next Steps

### Immediate

1. ✅ Install the application (done if you're reading this!)
2. ✅ Run the test suite to verify everything works
3. ✅ Try predicting an upcoming match
4. ✅ Check out player statistics

### Soon

1. Analyze a past match in the "Learn" tab
2. Export some predictions from the "Data" tab
3. Compare predictions with actual results
4. Provide feedback on accuracy

### Future

1. Track your prediction accuracy
2. Experiment with different analysis methods
3. Contribute improvements
4. Share insights with the community

## 💡 Tips & Tricks

### For Better Predictions

1. **Check Match Date**: Verify the match date on the website matches your expectations
2. **Playing XI**: Predictions are more accurate with confirmed lineups vs squads
3. **Historical Analysis**: Use "Learn" tab to understand prediction patterns
4. **Multiple Matches**: Analyze several matches to identify consistent patterns

### For Developers

1. **Debug Mode**: Set `headless=False` in CricketDataScraper to see browser
2. **Caching**: Streamlit caches expensive operations automatically
3. **Testing**: Run tests before committing: `python test_functionality.py`
4. **Logging**: Use `print()` or `st.write()` for debugging (shown in terminal/UI)

## 🎉 Success Checklist

- [ ] Application installed successfully
- [ ] Tests passing (run `python test_functionality.py`)
- [ ] Application opens in browser
- [ ] Can see upcoming matches
- [ ] Can run analysis on a match
- [ ] Can view player statistics
- [ ] Can access past matches in Learn tab
- [ ] Can export data

Once all checkboxes are checked, you're ready to go! 🚀

## 📞 Support

- **Documentation**: Check the docs in this repository
- **Issues**: Create a GitHub issue for bugs
- **Questions**: Ask in GitHub Discussions
- **Updates**: Watch the repository for new features

## 🙏 Thank You

Thank you for using Crick-Predict! We hope the new features make your cricket prediction experience better.

Happy Predicting! 🏏🎯

---

**Version**: 2.0.0 - Major Refactor
**Last Updated**: December 2025
**Status**: Production Ready ✅

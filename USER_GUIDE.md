# Crick-Predict User Guide

A comprehensive guide to using the Crick-Predict application with screenshots and detailed instructions.

## 📑 Table of Contents
- [Overview](#overview)
- [Application Interface](#application-interface)
- [Navigation Guide](#navigation-guide)
- [Feature-by-Feature Guide](#feature-by-feature-guide)
- [Filters and Options](#filters-and-options)
- [Tips and Best Practices](#tips-and-best-practices)
- [Troubleshooting](#troubleshooting)

---

## Overview

Crick-Predict is a cricket match prediction application that uses numerology and biorhythm analysis to predict player performance. The application features a modern, intuitive interface with multiple pages for different functionalities.

### Main Interface

![Main Application Interface](https://github.com/user-attachments/assets/59288b4d-5604-4a71-b04e-252d43fafcb5)

The application has four main sections accessible via the sidebar:
- 🏏 **App** - Main prediction interface
- 📊 **Player Stats** - View individual player statistics
- 🎓 **Learn** - Analyze past matches
- ℹ️ **Data** - Export and view prediction data

---

## Application Interface

### Layout Overview

```
┌─────────────────────────────────────────────────────────────┐
│  [Deploy]                                              [≡]   │ Top Bar
├──────────┬──────────────────────────────────────────────────┤
│          │                                                   │
│  🏏 App  │           Main Content Area                       │
│          │                                                   │
│  📊 Player Stats │   • Match Selection                      │
│          │   • Analysis Controls                             │
│  🎓 Learn│   • Results Display                               │
│          │   • Charts and Visualizations                     │
│  ℹ️ Data │                                                   │
│          │                                                   │
│ Sidebar  │           (Content changes per page)              │
└──────────┴──────────────────────────────────────────────────┘
```

### Navigation Sidebar

Located on the left side of the screen, the sidebar provides quick access to all major features:

**Icons and Labels:**
- 🏏 **App** - Predict upcoming matches
- 📊 **Player Stats** - View player information and statistics
- 🎓 **Learn** - Analyze completed matches for learning
- ℹ️ **Data** - Export and manage prediction data

---

## Navigation Guide

### Switching Between Pages

1. **Click on any sidebar item** to navigate to that page
2. **Active page** is highlighted in the sidebar
3. **URL changes** to reflect current page (e.g., `/player_stats`)
4. **State is preserved** when switching between pages

### Page URLs

- Main App: `http://localhost:8501/`
- Player Stats: `http://localhost:8501/player_stats`
- Learn: `http://localhost:8501/debug`
- Data: `http://localhost:8501/data_down`

---

## Feature-by-Feature Guide

## 1. 🏏 App Page - Match Prediction

### Purpose
Predict player performance for upcoming cricket matches using numerology and biorhythm analysis.

### Interface Components

#### A. Header Section
```
Dream11 Cricket
[Current Date and Time Display]
```
- Shows application title
- Displays current date/time for reference

#### B. Match Selection
```
Match: [Dropdown Menu                    ▼]
```
**Functionality:**
- Lists all upcoming cricket matches
- Format: "Team A vs Team B @YYYY-MM-DD"
- Automatically fetches latest fixtures from ESPN Cricinfo
- Updates dynamically

**How to Use:**
1. Click on the dropdown
2. Browse through available matches
3. Select your desired match
4. Match URL is automatically loaded

#### C. Analysis Type Selection
```
Analysis Type: [numerology                ▼]
```
**Options:**
- **numerology** - Uses numerology and biorhythm calculations (default)
- *(Future: Additional analysis methods may be added)*

#### D. Control Buttons
```
[Start]  [Reset]
```

**Start Button:**
- Triggers the analysis for selected match
- Fetches player lineup
- Retrieves birth dates
- Calculates biorhythm values
- Displays results with charts

**Reset Button:**
- Clears current analysis
- Resets session data
- Returns to initial state
- Shows success message when cleared

### Step-by-Step Usage

#### Step 1: Select a Match
1. Open the **Match** dropdown
2. Review available matches with dates
3. Click to select your match of interest

**Example:**
```
India vs Australia @2025-01-15
Pakistan vs England @2025-01-16
New Zealand vs South Africa @2025-01-17
```

#### Step 2: Choose Analysis Type
1. Keep default "numerology" or select another (if available)
2. This determines the calculation method used

#### Step 3: Start Analysis
1. Click the **[Start]** button
2. Wait for analysis to complete (may take 1-2 minutes)
3. Progress indicators show:
   - "Getting bdata of [player name]"
   - Spinner animations during data fetch

#### Step 4: View Results

**For Each Player, You'll See:**

**A. Player Header**
```
# [Player Full Name]
```

**B. Personal Information**
```
Name: [Full Name]
DOB: YYYY-MM-DDTHH:MM:SS.000000Z
```

**C. Numerology Numbers**
```
Bhagyank: [1-9]
Naamank: [1-9]
Moolank: [1-9]
```

**Definitions:**
- **Bhagyank (Destiny Number)**: Sum of all birth date digits
- **Naamank (Name Number)**: Numerological value of the name
- **Moolank (Root Number)**: Sum of birth date digits only

**D. Combined Formula**
```
[Bhagyank] + ([Moolank] × [Naamank]) = [Combined Score]
```

**E. Date-wise Biorhythm Table**
```
------------------------------------------------------
Date          | Values
------------------------------------------------------
DD-MM-YYYY   | [Biorhythm Value between -1 and 1]
...
```
Shows 30 days (-15 to +14 from match date)

**F. Match Day Value**
```
BIO: [Value for Match Day]
```
- **Higher values (closer to 1)** = Better predicted performance
- **Lower values (closer to -1)** = Lower predicted performance
- **Values near 0** = Neutral performance

**G. Biorhythm Chart**

Visual sine wave showing player's biorhythm cycle:
- **X-axis**: Dates (15 days before to 14 days after)
- **Y-axis**: Biorhythm level (-1 to 1)
- **Peak**: Best performance predicted
- **Trough**: Lowest performance predicted
- **Match day** highlighted

**H. Performance Indicators**

```
"Great.." - Positive trend detected
"Flop :(" - Negative trend detected
"Warning!! Prediction may fail!" - Unstable biorhythm
"Pipe!" - Repeated patterns detected
```

#### Step 5: Review All Players
- Scroll through results for all players in both teams
- Compare biorhythm values
- Note players with peak performance on match day

#### Step 6: Export Data (Optional)
- Navigate to **Data** page
- Download CSV with all biorhythm values
- Compare with Dream11 top picks

---

## 2. 📊 Player Stats Page

### Purpose
View detailed statistics and information for any cricket player.

### Interface Components

#### A. Header
```
🏏 Player Statistics
Get detailed statistics for any cricket player
```

#### B. Input Section
```
Enter Player Profile URL
[https://www.espncricinfo.com/cricketers/player-name-12345]

[Get Player Stats]
```

**Input Field:**
- Accepts ESPN Cricinfo player profile URLs
- Placeholder shows format example
- Validation on submission

#### C. Results Display

**Two-Column Layout:**

**Left Column - Basic Information:**
```
Name: [Player Full Name]
Country: [Country Name]
Playing Role: [Batsman/Bowler/All-rounder/Wicketkeeper]
Date of Birth: [DD/MM/YYYY]
```

**Right Column - Playing Style:**
```
Batting Style: [Right-hand/Left-hand bat]
Bowling Style: [Fast/Spin/Medium/N/A]
```

#### D. Match Statistics
```
Recent Matches: [Number]
```
- Shows count of recent matches played
- Updated from player profile

### Step-by-Step Usage

#### Step 1: Get Player URL
1. Go to ESPN Cricinfo website
2. Search for player name
3. Open player profile page
4. Copy the URL from browser address bar

**URL Format:**
```
https://www.espncricinfo.com/cricketers/[player-name]-[player-id]

Example:
https://www.espncricinfo.com/cricketers/virat-kohli-253802
```

#### Step 2: Enter URL
1. Navigate to **Player Stats** page
2. Paste URL into input field
3. Verify URL is complete and correct

#### Step 3: Fetch Statistics
1. Click **[Get Player Stats]** button
2. Wait for browser to fetch data (5-10 seconds)
3. Spinner indicates loading

#### Step 4: Review Information

**Basic Information Section:**
- Verify player identity
- Check country and role
- Note date of birth (useful for numerology)

**Playing Style Section:**
- Understand player's batting preference
- Check bowling type and style
- Helps in team selection

**Match Statistics:**
- See recent activity level
- Gauge current form
- Compare with other players

### Use Cases

**For Match Prediction:**
- Get DOB for manual numerology calculation
- Verify player role and capability
- Check recent match activity

**For Team Selection:**
- Compare multiple players side-by-side
- Check playing styles compatibility
- Verify player information

**For Analysis:**
- Gather player data for records
- Build player database
- Historical tracking

---

## 3. 🎓 Learn Page - Past Match Analysis

### Purpose
Analyze completed matches to learn from predictions and improve accuracy.

### Interface Components

#### A. Header
```
Dream11 Cricket Review
[Current Date and Time]
```

#### B. Match Selection
```
Match: [Dropdown - Completed Matches      ▼]
```
- Lists recently completed matches
- Format: "Team A vs Team B @YYYY-MM-DD"
- Fetches from ESPN Cricinfo results page

#### C. Analysis Controls
```
Analysis Type: [numerology                ▼]

[Start]  [Reset]
```

Similar to main App page but for past matches

#### D. MVP Section
```
MVP
[Table showing Most Valuable Players]
```
Shows actual match MVPs from ESPN Cricinfo

### Step-by-Step Usage

#### Step 1: Select Completed Match
1. Open **Match** dropdown
2. Review list of completed matches
3. Select match you want to analyze

#### Step 2: Start Analysis
1. Click **[Start]** button
2. Application shows:
   - MVP list (actual match performers)
   - Numerology analysis for all players
   - Biorhythm values for match day

#### Step 3: Compare Results

**Compare Prediction vs Actual:**

1. **Review MVP List**
   - See who actually performed well
   - Note their names and positions

2. **Check Biorhythm Values**
   - Find MVPs in your analysis
   - Check their biorhythm value on match day
   - Were high values = high performance?

3. **Identify Patterns**
   - Did players with peak biorhythm perform well?
   - Were there any anomalies?
   - What was the correlation?

4. **Learn from Mismatches**
   - Players with high biorhythm but poor performance
   - Players with low biorhythm but great performance
   - Consider external factors (pitch, weather, etc.)

#### Step 4: Document Insights
- Take notes on patterns
- Track accuracy percentage
- Refine your selection strategy

### Benefits of Learn Mode

**Validation:**
- Verify prediction accuracy
- Build confidence in the method
- Identify limitations

**Pattern Recognition:**
- Spot consistent performers
- Recognize team trends
- Understand form cycles

**Strategy Development:**
- Refine player selection
- Balance biorhythm with form
- Improve Dream11 team building

---

## 4. ℹ️ Data Page - Export and Analysis

### Purpose
Export prediction data and view Dream11 comparison data.

### Interface Components

#### A. Data Table Display
```
[Editable Data Table]

Columns:
- player: Player name
- prev: Biorhythm value (day before)
- today: Biorhythm value (match day)
- tom: Biorhythm value (day after)
- dream: Dream11 top pick indicator (checkbox)
```

#### B. Export Controls
```
[Download]
```
Downloads data as CSV file

#### C. MVP Comparison (if available)
```
URL: [Match Impact Player URL]
[DataFrame showing top performers]
```

### Step-by-Step Usage

#### Step 1: Generate Predictions
1. Go to **App** page first
2. Select match and run analysis
3. Wait for completion

#### Step 2: Navigate to Data Page
1. Click **Data** in sidebar
2. View generated data table

#### Step 3: Review Data

**Table Columns Explained:**

| Column | Description | Use |
|--------|-------------|-----|
| player | Player full name | Identification |
| prev | Previous day biorhythm | Trend analysis |
| today | Match day biorhythm | Primary predictor |
| tom | Next day biorhythm | Trend continuation |
| dream | Dream11 top pick flag | Comparison marker |

#### Step 4: Edit Data (Optional)
1. Click on any cell to edit
2. Modify values if needed
3. Add notes or flags
4. Mark Dream11 selections

#### Step 5: Compare with Dream11
If available:
1. View MVP list comparison
2. Check which predictions matched Dream11 picks
3. Note accuracy

#### Step 6: Download CSV
1. Click **[Download]** button
2. File saves as `[match-name].csv`
3. Open in Excel/Sheets for analysis

### CSV File Format

```csv
player,prev,today,tom,dream
Player Name 1,0.8564,-0.3421,0.9876,False
Player Name 2,0.1234,0.9999,-0.4567,True
...
```

### Data Analysis Tips

**In Excel/Google Sheets:**

1. **Sort by 'today' column** (highest to lowest)
   - Identify top performers
   - Quick visual ranking

2. **Filter players with today > 0.7**
   - High biorhythm players only
   - Potential captain/vice-captain

3. **Check trend (prev → today → tom)**
   - Rising trend = improving form
   - Falling trend = declining form
   - Stable = consistent

4. **Compare dream column**
   - True = Dream11 picked them
   - False = Not in Dream11 top picks
   - Calculate match percentage

5. **Create visualizations**
   - Bar charts for biorhythm values
   - Line charts for trends
   - Scatter plots for correlations

---

## Filters and Options

### Match Filters

**On App and Learn Pages:**

**Date Filter:**
- Matches automatically filtered by date
- Upcoming matches on App page
- Completed matches on Learn page
- Sorted chronologically

**Team Filter:**
- Use browser search (Ctrl+F / Cmd+F)
- Type team name to find specific matches
- Dropdown shows all available matches

### Analysis Options

**Analysis Type Dropdown:**

Currently available:
- **numerology** - Numerology + Biorhythm method

Future options may include:
- Astrology-based analysis
- Statistical modeling
- Machine learning predictions
- Combined methods

### Display Options

**Data Table Filters:**

1. **Column Visibility:**
   - All columns shown by default
   - Can be hidden/shown in future versions

2. **Sorting:**
   - Click column headers to sort
   - Ascending/descending order
   - Multi-column sort available

3. **Search/Filter:**
   - Use data editor features
   - Filter by player name
   - Filter by value ranges

### Export Options

**CSV Export:**
- File name: `[match-name].csv`
- Format: Standard CSV
- Encoding: UTF-8
- Opens in: Excel, Google Sheets, Python, R

---

## Tips and Best Practices

### For Accurate Predictions

1. **Use Confirmed Lineups**
   - Wait for official playing XI
   - Squad predictions less accurate
   - Check team announcements

2. **Consider External Factors**
   - Pitch conditions
   - Weather forecast
   - Team strategy
   - Recent form

3. **Analyze Multiple Matches**
   - Don't rely on single prediction
   - Study patterns over time
   - Build experience

4. **Combine with Other Methods**
   - Check player stats
   - Review recent performances
   - Read expert opinions
   - Use multiple prediction tools

### For Dream11 Selection

1. **Identify Peak Performers**
   - Sort by biorhythm value
   - Focus on players > 0.7
   - Consider trend (rising/falling)

2. **Balance Your Team**
   - Don't pick all high biorhythm
   - Include role diversity
   - Consider team composition rules

3. **Captain/Vice-Captain Selection**
   - Highest biorhythm + good form
   - Recent performance history
   - Favorable matchup

4. **Track and Learn**
   - Record your teams
   - Compare predictions vs results
   - Adjust strategy over time

### For Data Analysis

1. **Export Regularly**
   - Save data after each prediction
   - Build historical database
   - Track accuracy metrics

2. **Maintain Records**
   - Create spreadsheet tracker
   - Log match dates and results
   - Calculate success rates

3. **Compare Methods**
   - Try different analysis types
   - Compare with other tools
   - Find what works for you

### For Best Performance

1. **Stable Internet Connection**
   - Required for data fetching
   - Browser scraping needs bandwidth
   - Avoid during outages

2. **Allow Time for Analysis**
   - First run may take 2-3 minutes
   - Subsequent faster (caching)
   - Don't interrupt process

3. **Keep Browser Updated**
   - Playwright uses Chromium
   - Updates improve stability
   - Run `playwright install chromium` periodically

---

## Troubleshooting

### Common Issues

#### "No matches found"
**Causes:**
- Network connectivity issue
- ESPN Cricinfo temporary down
- No scheduled matches today

**Solutions:**
- Check internet connection
- Try again in few minutes
- Check ESPN Cricinfo directly

#### "Squad not available"
**Causes:**
- Match too far in future
- Teams not announced yet
- Page structure changed

**Solutions:**
- Wait for official announcement
- Try closer to match date
- Use Learn page for past matches

#### "DOB not found"
**Causes:**
- Player profile incomplete
- New player
- Database issue

**Solutions:**
- Player skipped in analysis
- Others still processed
- Report if persists

#### Analysis taking too long
**Causes:**
- Slow internet
- Many players (20+)
- Server load

**Solutions:**
- Be patient (2-3 minutes normal)
- Check network speed
- Try during off-peak hours

#### CSV not downloading
**Causes:**
- Browser download block
- No data generated yet
- Permission issue

**Solutions:**
- Allow downloads in browser
- Run analysis first
- Check download folder

### Error Messages

#### "Error: Page.goto: net::ERR_NAME_NOT_RESOLVED"
**Meaning:** Cannot reach ESPN Cricinfo
**Solution:** Check internet connection, firewall settings

#### "Error: Player data not found"
**Meaning:** Couldn't fetch player information
**Solution:** Verify player URL, try different player

#### "Warning!! Prediction may fail!"
**Meaning:** Biorhythm values are unstable
**Solution:** Use caution, consider other factors

### Getting Help

1. **Check Documentation**
   - README.md
   - INSTALLATION.md
   - WORKFLOW_GUIDE.md

2. **Run Tests**
   ```bash
   python test_functionality.py
   ```

3. **Check Logs**
   - Look for error messages
   - Note exact steps to reproduce
   - Check network connectivity

4. **Report Issues**
   - GitHub Issues page
   - Include error messages
   - Describe what you were doing
   - Mention OS and Python version

---

## Keyboard Shortcuts

### General Navigation
- **Tab** - Move between fields
- **Enter** - Submit/Confirm
- **Esc** - Close dialogs
- **Ctrl/Cmd + F** - Find in page

### Data Table
- **Arrow Keys** - Navigate cells
- **Enter** - Edit cell
- **Tab** - Next cell
- **Shift + Tab** - Previous cell

### Browser
- **Ctrl/Cmd + R** - Refresh page
- **Ctrl/Cmd + W** - Close tab
- **Ctrl/Cmd + T** - New tab

---

## Video Tutorials

*(Future: Add video links here when available)*

- Getting Started with Crick-Predict
- Making Your First Prediction
- Understanding Biorhythm Charts
- Building Your Dream11 Team
- Analyzing Past Matches

---

## Glossary

**Bhagyank (भाग्यांक):**
Destiny number calculated from complete date of birth. Represents life path.

**Biorhythm:**
Cyclical pattern of human life. Physical, emotional, and intellectual cycles.

**Moolank (मूलांक):**
Root number calculated from birth date only. Represents core personality.

**Naamank (नामांक):**
Name number calculated from letters. Represents identity.

**MVP (Most Valuable Player):**
Player with best performance in a match. Awarded by official scorers.

**Combined Score:**
Formula combining all numerology numbers. Used for biorhythm calculation.

**Playing XI:**
Confirmed team of 11 players starting the match.

**Squad:**
Full team including reserves. Larger than playing XI.

---

## FAQ

**Q: How accurate are the predictions?**
A: Numerology is for entertainment. Real match outcomes depend on many factors. Use as one of multiple tools.

**Q: Can I use this for betting?**
A: This is for entertainment and Dream11 fantasy cricket only. Not for real-money betting.

**Q: How often are fixtures updated?**
A: Live fetched from ESPN Cricinfo. Always current when you load the page.

**Q: Can I analyze women's cricket?**
A: Yes! Works for all cricket matches on ESPN Cricinfo.

**Q: Does it work offline?**
A: No. Requires internet to fetch match and player data.

**Q: Can I export to PDF?**
A: Currently CSV only. Open in Excel and export to PDF if needed.

**Q: How do I improve accuracy?**
A: Use Learn page to study patterns. Combine with other analysis methods.

**Q: Is my data stored?**
A: No. Everything is temporary. Close browser and all data is gone.

**Q: Can I contribute features?**
A: Yes! See WORKFLOW_GUIDE.md for developer information.

**Q: Mobile app available?**
A: Currently web only. Mobile browsers supported but desktop recommended.

---

## Contact & Support

- **GitHub Repository:** https://github.com/djmahe4/Crick-Predict
- **Issues:** Report bugs on GitHub Issues
- **Documentation:** All .md files in repository
- **Updates:** Watch repository for new releases

---

## Version Information

**Document Version:** 1.0
**Application Version:** 2.0.0
**Last Updated:** December 2025
**Compatible With:** All platforms (Windows, Linux, macOS)

---

## Appendix

### Sample Workflow

**Complete Process from Start to Finish:**

1. **Install Application** (one-time)
   - Run installation script
   - Verify tests pass
   - Launch application

2. **Select Upcoming Match**
   - Open App page
   - Browse matches
   - Select match of interest

3. **Run Analysis**
   - Click Start
   - Wait for completion
   - Review all players

4. **Export Data**
   - Navigate to Data page
   - Download CSV
   - Open in spreadsheet

5. **Build Dream11 Team**
   - Sort by biorhythm values
   - Select top performers
   - Balance team composition
   - Choose captain/vice-captain

6. **Track Results**
   - After match, go to Learn page
   - Select same match
   - Compare predictions vs actual
   - Calculate accuracy

7. **Improve Strategy**
   - Note what worked
   - Adjust selection criteria
   - Combine with other methods
   - Repeat and refine

---

**Happy Predicting! 🏏🎯**

*Remember: This is for entertainment and fantasy cricket only. Real match outcomes depend on numerous factors including skill, form, conditions, and chance.*

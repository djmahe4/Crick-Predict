# Workflow Guide for Crick-Predict

This document explains how the application works, its architecture, and the workflow separation implemented.

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Module Breakdown](#module-breakdown)
- [Data Scraping Workflow](#data-scraping-workflow)
- [Numerology Analysis Workflow](#numerology-analysis-workflow)
- [Player Statistics Workflow](#player-statistics-workflow)
- [For Developers](#for-developers)

---

## Architecture Overview

The application follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit UI Layer                        │
│  (app.py, debug.py)                                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               Business Logic Layer                           │
│  (numerology.py)                                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            Data Scraping Workflow Layer                      │
│  (cricket_workflow.py)                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│          Browser Automation (Playwright)                     │
│  Live browser-based data fetching from ESPN Cricinfo        │
└─────────────────────────────────────────────────────────────┘
```

---

## Module Breakdown

### 1. **app.py** - Main Application UI
- **Purpose**: Primary Streamlit interface for match prediction
- **Key Features**:
  - Match selection from upcoming fixtures
  - Numerology analysis trigger
  - Player statistics viewer
  - Navigation between different pages
- **Dependencies**: `cricket_workflow`, `numerology`, `debug`

### 2. **cricket_workflow.py** - Data Scraping Module
- **Purpose**: Handles all data fetching using live browser automation
- **Key Components**:
  - `CricketDataScraper`: Main class for browser-based scraping
  - `scraper()`: General-purpose page scraper
  - `matches()`: Fetch upcoming match fixtures
  - `debug_matches()`: Fetch completed match results
  - `get_player_stats()`: Get detailed player statistics
  - `get_player_match_count()`: Get match count for a player
  - `birth_get()`: Batch fetch birth data for multiple players
  - `match11()`: Get match lineup (playing XI or squad)

**Why Browser-Based Scraping?**
- More reliable than HTTP-only requests
- Handles JavaScript-rendered content
- Can wait for dynamic elements to load
- Better mimics real user behavior
- Reduces chance of being blocked

### 3. **numerology.py** - Analysis Logic
- **Purpose**: Numerology and biorhythm calculations
- **Key Functions**:
  - `calculate_bhagyank()`: Calculate destiny number
  - `calculate_moolank()`: Calculate root number
  - `calculate_naamank()`: Calculate name number
  - `biorhythm_chart()`: Generate biorhythm data
  - `plot_biorhythm_chart()`: Visualize biorhythm charts
  - `main()`: Main orchestration function
- **Dependencies**: Uses `cricket_workflow` for data fetching

### 4. **debug.py** - Past Match Analysis
- **Purpose**: Learn from past matches
- **Key Features**:
  - Fetch completed match results
  - Analyze player performance retrospectively
  - View MVP (Most Valuable Player) lists
  - Compare predictions with actual results

### 5. **test.py** - Compatibility Layer
- **Purpose**: Maintains backward compatibility
- **Implementation**: Wrapper that imports from `cricket_workflow.py`
- **Why?**: Allows existing code to continue working without changes

---

## Data Scraping Workflow

### 1. Fetching Match Fixtures

```python
from cricket_workflow import matches

# Get upcoming matches
fixtures = matches()
# Returns: {"Team A vs Team B @2025-01-20": "https://..."}
```

**Workflow**:
1. Browser navigates to ESPN Cricinfo fixtures page
2. Waits for JavaScript to render match data
3. Extracts `__NEXT_DATA__` JSON from page
4. Parses match information
5. Returns dictionary of match descriptions to URLs

### 2. Getting Match Lineup

```python
from cricket_workflow import match11

# Get playing XI or squad
players, match_date = match11(match_url)
# Returns: ({player_name: player_url}, (start_time, timezone))
```

**Workflow**:
1. Try to fetch playing XI first
2. If not available, fallback to squad
3. Extract player URLs from both teams
4. Get match start time and timezone
5. Return player dictionary and match metadata

### 3. Fetching Player Birth Data

```python
from cricket_workflow import birth_get

# Get birth data for multiple players
birth_data = birth_get(player_dict)
# Returns: {full_name: date_of_birth_dict}
```

**Workflow**:
1. Iterate through player URLs
2. For each player:
   - Navigate to profile page
   - Extract birth date information
   - Store full name and long name mappings
3. Return consolidated birth data

### 4. Getting Player Statistics

```python
from cricket_workflow import get_player_stats

# Get detailed player stats
stats = get_player_stats(player_url)
# Returns: {name, country, role, batting_style, ...}
```

**Workflow**:
1. Navigate to player profile
2. Extract player metadata
3. Parse playing role and styles
4. Get career statistics if available
5. Return structured data

---

## Numerology Analysis Workflow

### Complete Analysis Flow

```
User selects match
       ↓
Fetch match lineup (cricket_workflow)
       ↓
Get player birth dates (cricket_workflow)
       ↓
For each player:
    ├─ Calculate Moolank (date of birth)
    ├─ Calculate Bhagyank (full DOB sum)
    ├─ Calculate Naamank (name value)
    ├─ Combine numbers with formula
    ├─ Calculate biorhythm for match date
    ├─ Generate chart data (-15 to +14 days)
    └─ Display results and visualization
       ↓
Store results in session state
       ↓
Allow data export
```

### Numerology Calculations

**Moolank (Root Number)**:
```python
# Sum of birth date digits reduced to single digit
Date: 15 → 1 + 5 = 6
```

**Bhagyank (Destiny Number)**:
```python
# Sum of all DOB digits reduced to single digit
DOB: 15/10/1990
→ 1+5+1+0+1+9+9+0 = 26 → 2+6 = 8
```

**Naamank (Name Number)**:
```python
# Sum of name values + adjustment
# Using Chaldean numerology mapping
```

**Combined Score**:
```python
combined = bhagyank + (moolank * naamank)
```

**Biorhythm**:
```python
biorhythm[day] = sin(2π * day / combined)
```

---

## Player Statistics Workflow

### Available Statistics

1. **Basic Information**:
   - Full name
   - Country
   - Date of birth
   - Playing role (Batsman, Bowler, All-rounder, etc.)

2. **Playing Style**:
   - Batting style (Right-hand, Left-hand)
   - Bowling style (Fast, Spin, etc.)

3. **Match History**:
   - Number of recent matches
   - Total matches played (if available)

### Usage in UI

1. Navigate to "Player Stats" page
2. Enter ESPN Cricinfo player URL
3. Click "Get Player Stats"
4. View formatted statistics

---

## For Developers

### Adding New Features

#### 1. Adding New Scraping Function

```python
# In cricket_workflow.py

def get_new_data(url):
    """
    Scrape new type of data.
    
    Args:
        url: Target URL
        
    Returns:
        dict: Extracted data
    """
    data = scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    # Extract data
    return extracted_data
```

#### 2. Adding New UI Page

```python
# In app.py

def new_page():
    """New feature page."""
    st.title("New Feature")
    # Your UI code here

# Add to navigation
pg = st.navigation([
    st.Page(app, title="App", icon="🏏"),
    st.Page(new_page, title="New Feature", icon="🆕"),
    # ... other pages
])
```

### Testing

Always test new features:

```bash
# Run test suite
python test_functionality.py

# Test specific module
python -c "from cricket_workflow import new_function; new_function()"
```

### Debugging Browser Scraping

To debug browser scraping visually:

```python
from cricket_workflow import CricketDataScraper

# Run with headless=False to see browser
with CricketDataScraper(headless=False) as scraper:
    html = scraper.scrape_page(url)
```

---

## CI/CD Integration

The project includes automated workflows:

### Quick Check Workflow
- Runs on every commit
- Validates Python syntax
- Tests imports
- Quick browser functionality check

### Full Test Suite
- Runs on PR and main branch pushes
- Tests across Python 3.8-3.12
- Code quality checks (flake8, pylint)
- Security scanning (safety, bandit)
- Integration tests

### Running Locally

```bash
# Quick test
python test_functionality.py

# Full installation test
./install_linux.sh  # or install_windows.bat
```

---

## Best Practices

1. **Always use context manager for CricketDataScraper**:
   ```python
   with CricketDataScraper() as scraper:
       data = scraper.scrape_page(url)
   ```

2. **Handle scraping errors gracefully**:
   ```python
   try:
       data = scraper(url)
   except Exception as e:
       st.error(f"Failed to fetch data: {e}")
   ```

3. **Cache expensive operations**:
   ```python
   @st.cache_data
   def expensive_operation():
       # Long-running task
       pass
   ```

4. **Respect rate limits**:
   ```python
   import time
   time.sleep(1)  # Add delay between requests
   ```

---

## Troubleshooting

### Browser Fails to Launch
```bash
# Reinstall Playwright browsers
playwright install chromium
playwright install-deps chromium  # Linux only
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Scraping Timeout
```python
# Increase timeout
scraper = CricketDataScraper(timeout=60000)  # 60 seconds
```

---

## Future Enhancements

Potential areas for expansion:

1. **More Statistics**: Team rankings, head-to-head records
2. **Historical Analysis**: Compare predictions vs actual performance
3. **Machine Learning**: Use historical data for better predictions
4. **Live Match Updates**: Real-time score tracking
5. **Multiple Analysis Methods**: Add other prediction systems
6. **Player Comparison**: Side-by-side player comparisons
7. **Export Options**: PDF reports, Excel sheets
8. **User Accounts**: Save predictions and track accuracy

---

## Contributing

When contributing:

1. Follow the modular architecture
2. Add tests for new features
3. Update documentation
4. Ensure CI/CD passes
5. Use descriptive commit messages

---

## License

See LICENSE file for details.

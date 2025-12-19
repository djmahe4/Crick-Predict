"""
Cricket Workflow Module
Handles all cricket data scraping using live browser automation with Playwright.
Separated from Streamlit UI for better modularity.
"""

import json
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Optional streamlit import
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False


class CricketDataScraper:
    """Handles cricket data scraping using live browser automation."""
    
    def __init__(self, headless=True, timeout=30000):
        """
        Initialize the scraper.
        
        Args:
            headless: Whether to run browser in headless mode
            timeout: Default timeout for page operations in milliseconds
        """
        self.headless = headless
        self.timeout = timeout
        self.playwright = None
        self.browser = None
        self.context = None
        
    def __enter__(self):
        """Context manager entry."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
    
    def scrape_page(self, url, wait_for_selector='script#__NEXT_DATA__'):
        """
        Scrape a page using live browser.
        
        Args:
            url: URL to scrape
            wait_for_selector: CSS selector to wait for before extracting content
            
        Returns:
            HTML content of the page
        """
        page = self.context.new_page()
        try:
            page.goto(url, timeout=self.timeout, wait_until='networkidle')
            # Wait for the specific element that contains data
            page.wait_for_selector(wait_for_selector, timeout=self.timeout)
            content = page.content()
            return content
        except PlaywrightTimeoutError as e:
            print(f"Timeout error scraping {url}: {e}")
            # Try to get content anyway
            return page.content()
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            raise
        finally:
            page.close()


def scraper(url):
    """
    Scrape a URL using live browser automation.
    Replaces the old http.client based scraper.
    
    Args:
        url: URL to scrape
        
    Returns:
        bytes: HTML content of the page
    """
    with CricketDataScraper(headless=True) as scraper_obj:
        html_content = scraper_obj.scrape_page(url)
        return html_content.encode('utf-8')


def get_loc(url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'):
    """
    Get match location and timezone information.
    
    Args:
        url: Match URL
        
    Returns:
        tuple: (start_time, timezone)
    """
    data = scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    return (
        so['props']['appPageProps']['data']['data']['match']['startTime'],
        so['props']['appPageProps']['data']['data']['match']['ground']['town']['timezone']
    )


def match11sub(url):
    """
    Get player lineup from match page.
    
    Args:
        url: Match lineup URL
        
    Returns:
        dict: Dictionary of player names to their profile URLs
    """
    data = scraper(url)
    dic = {}
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    try:
        for player in so['props']["appPageProps"]["data"]["content"]["matchPlayers"]["teamPlayers"][0]['players']:
            dic.update({
                player["player"]["longName"]: 
                f"https://www.espncricinfo.com/cricketers/{player['player']['slug']}-{player['player']['objectId']}"
            })
        for player in so['props']["appPageProps"]["data"]["content"]["matchPlayers"]["teamPlayers"][1]['players']:
            dic.update({
                player["player"]["longName"]: 
                f"https://www.espncricinfo.com/cricketers/{player['player']['slug']}-{player['player']['objectId']}"
            })
    except (IndexError, KeyError):
        return {}
    
    return dic


def match11(url='https://www.espncricinfo.com/series/csa-4-day-series-division-1-2024-25-1444755/dolphins-vs-western-province-1st-match-1444880/full-scorecard', cond="match-playing-xi"):
    """
    Get match lineup and match date.
    
    Args:
        url: Match URL
        cond: Condition to use ("match-playing-xi" or "match-squads")
        
    Returns:
        tuple: (player_dict, match_date_info)
    """
    urll = url.split("/")
    urll[-1] = cond
    url = "/".join(urll)
    playerd = match11sub(url)
    print(playerd)
    if playerd == {} and cond == "match-squads":
        if HAS_STREAMLIT:
            st.write("Squads not available")
        raise Exception("Squad not found")
    elif playerd == {}:
        print("Lineup not available")
        playerd = match11(url, "match-squads")
    urll[-1] = 'live-cricket-score'
    nurl = "/".join(urll)
    mdate = get_loc(nurl)
    return playerd, mdate


def matches(url='https://www.espncricinfo.com/live-cricket-match-schedule-fixtures'):
    """
    Get list of upcoming matches.
    
    Args:
        url: Fixtures page URL
        
    Returns:
        dict: Dictionary of match descriptions to their URLs
    """
    data = scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    
    mids = {}
    for i in so['props']['appPageProps']['data']['data']['content']['matches']:
        mids.update({
            f"{i['teams'][0]['team']['name']} vs {i['teams'][1]['team']['name']} @{i['startDate'][:11]}":
            f"https://www.espncricinfo.com/series/{i['series']['slug']}-{i['series']['objectId']}/{i['slug']}-{i['objectId']}/live-cricket-score"
        })
    
    return mids


def debug_matches(url='https://www.espncricinfo.com/live-cricket-match-results'):
    """
    Get list of completed matches.
    
    Args:
        url: Results page URL
        
    Returns:
        dict: Dictionary of match descriptions to their URLs
    """
    data = scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    
    mids = {}
    for i in so['props']['appPageProps']['data']['data']['content']['matches']:
        mids.update({
            f"{i['teams'][0]['team']['name']} vs {i['teams'][1]['team']['name']} @{i['startDate'][:11]}":
            f"https://www.espncricinfo.com/series/{i['series']['slug']}-{i['series']['objectId']}/{i['slug']}-{i['objectId']}/live-cricket-score"
        })
    
    return mids


def get_player_stats(player_url):
    """
    Get detailed statistics for a player.
    
    Args:
        player_url: URL to player's profile page
        
    Returns:
        dict: Player statistics including matches played, runs, wickets, etc.
    """
    data = scraper(player_url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    
    try:
        player_data = so['props']['appPageProps']['data']['player']
        stats = {
            'name': player_data.get('fullName', 'N/A'),
            'longName': player_data.get('longName', 'N/A'),
            'dateOfBirth': player_data.get('dateOfBirth', None),
            'country': player_data.get('country', {}).get('name', 'N/A'),
            'battingStyle': player_data.get('battingStyles', [{}])[0].get('name', 'N/A') if player_data.get('battingStyles') else 'N/A',
            'bowlingStyle': player_data.get('bowlingStyles', [{}])[0].get('name', 'N/A') if player_data.get('bowlingStyles') else 'N/A',
            'playingRole': player_data.get('playingRole', {}).get('name', 'N/A'),
        }
        
        # Get career stats if available
        if 'recentMatches' in so['props']['appPageProps']['data']:
            recent_matches = so['props']['appPageProps']['data']['recentMatches']
            stats['recent_matches_count'] = len(recent_matches) if recent_matches else 0
        
        return stats
    except (KeyError, TypeError, IndexError) as e:
        print(f"Error extracting player stats: {e}")
        return {}


def get_team_stats(team_url):
    """
    Get team statistics.
    
    Args:
        team_url: URL to team's page
        
    Returns:
        dict: Team statistics
    """
    data = scraper(team_url)
    soup = BeautifulSoup(data, "html.parser")
    
    try:
        so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
        team_data = so['props']['appPageProps']['data']['team']
        
        stats = {
            'name': team_data.get('name', 'N/A'),
            'country': team_data.get('country', {}).get('name', 'N/A'),
            'teamType': team_data.get('teamType', {}).get('name', 'N/A'),
        }
        
        return stats
    except (KeyError, TypeError, IndexError) as e:
        print(f"Error extracting team stats: {e}")
        return {}


def get_player_match_count(player_url):
    """
    Get the number of matches played by a player across formats.
    
    Args:
        player_url: URL to player's profile page
        
    Returns:
        dict: Match counts by format (Tests, ODIs, T20Is, etc.)
    """
    data = scraper(player_url)
    soup = BeautifulSoup(data, "html.parser")
    
    try:
        so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
        
        # Try to get match counts from player stats
        match_counts = {
            'total': 0,
            'by_format': {}
        }
        
        # Look for career stats in the page data
        player_data = so['props']['appPageProps']['data'].get('player', {})
        
        if 'recentMatches' in so['props']['appPageProps']['data']:
            recent = so['props']['appPageProps']['data']['recentMatches']
            match_counts['recent_matches'] = len(recent) if recent else 0
        
        return match_counts
    except (KeyError, TypeError, IndexError) as e:
        print(f"Error extracting match count: {e}")
        return {'total': 0, 'by_format': {}}


def get_player_birth_data(player_url):
    """
    Get player's birth data and name.
    
    Args:
        player_url: URL to player's profile page
        
    Returns:
        tuple: (full_name, date_of_birth_dict, long_name)
    """
    data = scraper(player_url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    
    try:
        player = so['props']['appPageProps']['data']['player']
        return (
            player['fullName'],
            player['dateOfBirth'],
            player['longName']
        )
    except (KeyError, TypeError):
        return (None, None, None)


def birth_get(player_dict):
    """
    Get birth data for multiple players.
    
    Args:
        player_dict: Dictionary of player names to their URLs
        
    Returns:
        dict: Dictionary of full names to birth dates
    """
    bdata = {}
    names_mapping = {}
    
    for player_name, player_url in player_dict.items():
        try:
            if HAS_STREAMLIT:
                with st.spinner(f"Getting birth data of {player_name}"):
                    time.sleep(0.5)  # Small delay to avoid overwhelming the server
                    full_name, dob, long_name = get_player_birth_data(player_url)
                    
                    if full_name and dob:
                        bdata[full_name] = dob
                        names_mapping[long_name] = full_name
            else:
                full_name, dob, long_name = get_player_birth_data(player_url)
                if full_name and dob:
                    bdata[full_name] = dob
                    names_mapping[long_name] = full_name
        except Exception as e:
            print(f"Error getting birth data for {player_name}: {e}")
            continue
    
    # Store names mapping in session state if streamlit is available
    if HAS_STREAMLIT and hasattr(st, 'session_state'):
        st.session_state.names.update(names_mapping)
    
    return bdata

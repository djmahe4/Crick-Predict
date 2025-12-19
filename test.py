"""
Compatibility wrapper for cricket_workflow module.
This file maintains backward compatibility with existing code.
All functionality has been moved to cricket_workflow.py with live browser scraping.
"""

from cricket_workflow import (
    get_loc,
    match11,
    match11sub,
    matches,
    debug_matches,
    scraper,
    get_player_stats,
    get_team_stats,
    get_player_match_count,
    birth_get
)

# Export all functions for backward compatibility
__all__ = [
    'get_loc',
    'match11',
    'match11sub', 
    'matches',
    'debug_matches',
    'scraper',
    'get_player_stats',
    'get_team_stats',
    'get_player_match_count',
    'birth_get'
]

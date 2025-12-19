#!/usr/bin/env python3
"""
Test script to verify Crick-Predict functionality.
This can be run locally or in CI/CD pipelines.

Usage:
    python test_functionality.py
"""

import sys
import traceback


def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    try:
        import streamlit
        print(f"  ✓ Streamlit {streamlit.__version__}")
    except ImportError as e:
        print(f"  ✗ Streamlit import failed: {e}")
        return False
    
    try:
        import playwright
        print(f"  ✓ Playwright")
    except ImportError as e:
        print(f"  ✗ Playwright import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print(f"  ✓ Pandas {pd.__version__}")
    except ImportError as e:
        print(f"  ✗ Pandas import failed: {e}")
        return False
    
    try:
        import matplotlib
        print(f"  ✓ Matplotlib {matplotlib.__version__}")
    except ImportError as e:
        print(f"  ✗ Matplotlib import failed: {e}")
        return False
    
    try:
        from bs4 import BeautifulSoup
        print(f"  ✓ BeautifulSoup4")
    except ImportError as e:
        print(f"  ✗ BeautifulSoup4 import failed: {e}")
        return False
    
    try:
        import pytz
        print(f"  ✓ Pytz")
    except ImportError as e:
        print(f"  ✗ Pytz import failed: {e}")
        return False
    
    print("All core imports successful!\n")
    return True


def test_module_imports():
    """Test that custom modules can be imported."""
    print("Testing custom module imports...")
    try:
        from cricket_workflow import (
            CricketDataScraper, scraper, matches, debug_matches,
            get_player_stats, get_player_match_count, birth_get
        )
        print("  ✓ cricket_workflow module")
    except ImportError as e:
        print(f"  ✗ cricket_workflow import failed: {e}")
        traceback.print_exc()
        return False
    
    try:
        from numerology import main
        print("  ✓ numerology module")
    except ImportError as e:
        print(f"  ✗ numerology import failed: {e}")
        traceback.print_exc()
        return False
    
    try:
        from test import matches as test_matches
        print("  ✓ test module")
    except ImportError as e:
        print(f"  ✗ test import failed: {e}")
        traceback.print_exc()
        return False
    
    try:
        from debug import debug
        print("  ✓ debug module")
    except ImportError as e:
        print(f"  ✗ debug import failed: {e}")
        traceback.print_exc()
        return False
    
    print("All custom modules imported successfully!\n")
    return True


def test_cricket_workflow():
    """Test basic cricket_workflow functionality."""
    print("Testing cricket_workflow functionality...")
    try:
        from cricket_workflow import CricketDataScraper
        
        # Test class instantiation
        scraper = CricketDataScraper(headless=True, timeout=10000)
        print("  ✓ CricketDataScraper instantiation")
        
        # Test context manager
        with CricketDataScraper(headless=True, timeout=10000) as scraper_ctx:
            print("  ✓ CricketDataScraper context manager")
        
        print("cricket_workflow tests passed!\n")
        return True
    except Exception as e:
        print(f"  ✗ cricket_workflow test failed: {e}")
        traceback.print_exc()
        return False


def test_browser_automation():
    """Test that Playwright browser can be launched."""
    print("Testing browser automation...")
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("about:blank")
            page.close()
            browser.close()
        
        print("  ✓ Playwright browser launch successful")
        print("Browser automation test passed!\n")
        return True
    except Exception as e:
        print(f"  ✗ Browser automation test failed: {e}")
        print("  Note: You may need to run: playwright install chromium")
        traceback.print_exc()
        return False


def test_file_syntax():
    """Test that all Python files have valid syntax."""
    print("Testing file syntax...")
    import py_compile
    
    files_to_check = [
        'app.py',
        'cricket_workflow.py',
        'numerology.py',
        'debug.py',
        'test.py',
        'test_functionality.py'
    ]
    
    all_valid = True
    for file in files_to_check:
        try:
            py_compile.compile(file, doraise=True)
            print(f"  ✓ {file}")
        except py_compile.PyCompileError as e:
            print(f"  ✗ {file}: {e}")
            all_valid = False
    
    if all_valid:
        print("All Python files have valid syntax!\n")
    else:
        print("Some Python files have syntax errors!\n")
    
    return all_valid


def main():
    """Run all tests."""
    print("=" * 70)
    print("Crick-Predict Functionality Test Suite")
    print("=" * 70)
    print()
    
    tests = [
        ("File Syntax", test_file_syntax),
        ("Core Imports", test_imports),
        ("Module Imports", test_module_imports),
        ("Cricket Workflow", test_cricket_workflow),
        ("Browser Automation", test_browser_automation),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"Test '{test_name}' raised an exception: {e}")
            traceback.print_exc()
            results.append((test_name, False))
    
    print("=" * 70)
    print("Test Results Summary")
    print("=" * 70)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print("=" * 70)
    
    all_passed = all(result for _, result in results)
    if all_passed:
        print("All tests passed! ✓")
        return 0
    else:
        print("Some tests failed! ✗")
        return 1


if __name__ == "__main__":
    sys.exit(main())

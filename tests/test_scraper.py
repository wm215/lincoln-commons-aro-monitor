"""
Tests for the scraper module
"""
import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from scraper import main


def test_main_function():
    """Test that main function runs successfully"""
    result = main()
    assert result is True


def test_scraper_import():
    """Test that scraper module can be imported"""
    import scraper
    assert hasattr(scraper, "main")
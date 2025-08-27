"""
Tests for the scraper module
"""
import sys
import os

from scraper import main


def test_main_function():
    """Test that main function runs successfully"""
    result = main()
    assert result is True


def test_scraper_import():
    """Test that scraper module can be imported"""
    import scraper
    assert hasattr(scraper, "main")
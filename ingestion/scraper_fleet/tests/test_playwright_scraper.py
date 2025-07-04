import pytest
from infrastructure.playwright_scraper import PlaywrightReelsScraper
from domain.reel import Reel
from unittest.mock import patch
from datetime import datetime

@patch("infrastructure.playwright_scraper.sync_playwright")
def test_fetch_reels_by_hashtag_mocked(mock_sync_playwright):
    # Мокаем поведение Playwright: возвращаем заранее подготовленные данные
    class DummyPage:
        def goto(self, *a, **kw): pass
        def wait_for_selector(self, *a, **kw): pass
        def eval_on_selector_all(self, *a, **kw): return ["https://instagram.com/reel/1/"]
        def eval_on_selector(self, selector, script):
            if selector == "header a": return "author"
            if selector == "span[role='link']": return "desc"
            if selector == "section span": return "42"
            if selector == "video": return "http://example.com/video.mp4"
            if selector == "time": return "2024-01-01T00:00:00Z"
            return None
    class DummyBrowser:
        def new_page(self): return DummyPage()
        def close(self): pass
    class DummyPlaywright:
        @property
        def chromium(self):
            class Chromium:
                def launch(self, headless=True): return DummyBrowser()
            return Chromium()
    mock_sync_playwright.return_value.__enter__.return_value = DummyPlaywright()

    scraper = PlaywrightReelsScraper(headless=True)
    reels = scraper.fetch_reels_by_hashtag("test", limit=1)
    assert len(reels) == 1
    assert isinstance(reels[0], Reel)
    assert reels[0].author == "author"
    assert reels[0].likes == 42
    assert isinstance(reels[0].posted_at, datetime)
    assert reels[0].posted_at == datetime(2024, 1, 1, 0, 0, 0)

@patch("infrastructure.playwright_scraper.sync_playwright")
def test_fetch_reels_by_hashtag_empty(mock_sync_playwright):
    class DummyPage:
        def goto(self, *a, **kw): pass
        def wait_for_selector(self, *a, **kw): pass
        def eval_on_selector_all(self, *a, **kw): return []
    class DummyBrowser:
        def new_page(self): return DummyPage()
        def close(self): pass
    class DummyPlaywright:
        @property
        def chromium(self):
            class Chromium:
                def launch(self, headless=True): return DummyBrowser()
            return Chromium()
    mock_sync_playwright.return_value.__enter__.return_value = DummyPlaywright()
    scraper = PlaywrightReelsScraper(headless=True)
    reels = scraper.fetch_reels_by_hashtag("test", limit=1)
    assert reels == []

@patch("infrastructure.playwright_scraper.sync_playwright")
def test_fetch_reels_by_hashtag_error(mock_sync_playwright):
    class DummyPage:
        def goto(self, *a, **kw): raise Exception("Playwright error")
        def wait_for_selector(self, *a, **kw): pass
        def eval_on_selector_all(self, *a, **kw): return []
    class DummyBrowser:
        def new_page(self): return DummyPage()
        def close(self): pass
    class DummyPlaywright:
        @property
        def chromium(self):
            class Chromium:
                def launch(self, headless=True): return DummyBrowser()
            return Chromium()
    mock_sync_playwright.return_value.__enter__.return_value = DummyPlaywright()
    scraper = PlaywrightReelsScraper(headless=True)
    reels = scraper.fetch_reels_by_hashtag("test", limit=1)
    assert reels == [] 
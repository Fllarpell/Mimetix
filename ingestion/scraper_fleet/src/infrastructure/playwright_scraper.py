from typing import List
from datetime import datetime
from playwright.sync_api import sync_playwright
from domain.reel import Reel
from domain.abstract_scraper import AbstractReelScraper
from common.constants import (
    INSTAGRAM_URL, REEL_LINK_SELECTOR, REEL_AUTHOR_SELECTOR, REEL_DESC_SELECTOR,
    REEL_LIKES_SELECTOR, REEL_VIDEO_SELECTOR, REEL_TIME_SELECTOR
)

class PlaywrightReelsScraper(AbstractReelScraper):
    """
    Scraper для сбора метаданных публичных рилсов по хэштегу с помощью Playwright.
    Реализует интерфейс AbstractReelScraper.
    """
    def __init__(self, headless: bool = True) -> None:
        self._headless = headless

    def fetch_reels_by_hashtag(self, hashtag: str, limit: int = 10) -> List[Reel]:
        """
        Собирает метаданные публичных рилсов по хэштегу.
        Args:
            hashtag: Хэштег без #
            limit: Максимальное количество рилсов
        Returns:
            List[Reel]: Список собранных рилсов
        """
        reels: List[Reel] = []
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self._headless)
            page = browser.new_page()
            url = f"{INSTAGRAM_URL}/explore/tags/{hashtag}/"
            page.goto(url, timeout=60000)
            page.wait_for_selector("article")
            reel_links = page.eval_on_selector_all(REEL_LINK_SELECTOR, "elements => elements.map(e => e.href)")
            for link in reel_links[:limit]:
                try:
                    page.goto(link, timeout=30000)
                    page.wait_for_selector(REEL_VIDEO_SELECTOR, timeout=10000)
                    reel_id = link.rstrip("/").split("/")[-1]
                    author = page.eval_on_selector(REEL_AUTHOR_SELECTOR, "el => el.textContent") or ""
                    description = page.eval_on_selector(REEL_DESC_SELECTOR, "el => el.textContent") or ""
                    likes = int(page.eval_on_selector(REEL_LIKES_SELECTOR, "el => el.textContent") or 0)
                    views = likes
                    video_url = page.eval_on_selector(REEL_VIDEO_SELECTOR, "el => el.src") or ""
                    posted_at_str = page.eval_on_selector(REEL_TIME_SELECTOR, "el => el.getAttribute('datetime')") or "1970-01-01T00:00:00Z"
                    posted_at = datetime.fromisoformat(posted_at_str.replace("Z", "+00:00"))
                    reels.append(
                        Reel(
                            id=reel_id,
                            author=author,
                            description=description,
                            likes=likes,
                            views=views,
                            url=video_url,
                            posted_at=posted_at
                        )
                    )
                except Exception:
                    continue
            browser.close()
        return reels 
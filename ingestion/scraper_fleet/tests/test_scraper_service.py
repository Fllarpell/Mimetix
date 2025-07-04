import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from application.scraper_service import ScraperService
from domain.reel import Reel
from domain.abstract_repository import AbstractReelRepository
from typing import List
import datetime

class DummyScraper:
    """Mock-скрейпер для тестов, реализует fetch_reels_by_hashtag."""
    def fetch_reels_by_hashtag(self, hashtag: str, limit: int = 2) -> List[Reel]:
        return [
            Reel(id="1", author="a", description="d", likes=1, views=2, url="u", posted_at="2024-01-01T00:00:00Z"),
            Reel(id="2", author="b", description="e", likes=3, views=4, url="v", posted_at="2024-01-02T00:00:00Z")
        ]

class DummyRepository(AbstractReelRepository):
    """Mock-репозиторий для тестов, реализует save/get_all."""
    def __init__(self):
        self.saved = []
    def save(self, reel: Reel) -> None:
        self.saved.append(reel)
    def get_all(self) -> List[Reel]:
        return self.saved

def test_collect_and_save_reels_by_hashtag():
    """Проверяет, что ScraperService корректно собирает и сохраняет рилсы."""
    repo = DummyRepository()
    scraper = DummyScraper()
    service = ScraperService(repo, scraper)
    reels = service.collect_and_save_reels_by_hashtag("test", limit=2)
    assert len(reels) == 2
    assert repo.get_all() == reels
    assert reels[0].author == "a"
    assert reels[1].author == "b"

def test_scraper_service_integration():
    """Интеграционный тест: ScraperService + DummyScraper + DummyRepository."""
    repo = DummyRepository()
    scraper = DummyScraper()
    service = ScraperService(repo, scraper)
    reels = service.collect_and_save_reels_by_hashtag("integration", limit=2)
    assert len(reels) == 2
    assert repo.get_all() == reels
    assert reels[0].author == "a"
    assert reels[1].author == "b"

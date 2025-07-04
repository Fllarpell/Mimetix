from typing import List
from domain.reel import Reel
from domain.abstract_repository import AbstractReelRepository
from infrastructure.playwright_scraper import PlaywrightReelsScraper

class ScraperService:
    """
    Сервис для сбора и сохранения рилсов (use-case layer).
    Интегрирует PlaywrightReelsScraper и AbstractReelRepository (например, S3).
    """
    def __init__(self, repository: AbstractReelRepository, scraper: PlaywrightReelsScraper) -> None:
        self._repository = repository
        self._scraper = scraper

    def collect_and_save_reels_by_hashtag(self, hashtag: str, limit: int = 10) -> List[Reel]:
        """
        Собирает рилсы по хэштегу и сохраняет их в хранилище.
        Args:
            hashtag: Хэштег без #
            limit: Максимальное количество рилсов
        Returns:
            List[Reel]: Список собранных и сохранённых рилсов
        """
        reels = self._scraper.fetch_reels_by_hashtag(hashtag, limit)
        for reel in reels:
            self._repository.save(reel)
        return reels

    def save_reels(self, reels: List[Reel]) -> None:
        """Сохраняет список рилсов через репозиторий."""
        for reel in reels:
            self._repository.save(reel) 
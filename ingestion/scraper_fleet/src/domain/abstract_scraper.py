from abc import ABC, abstractmethod
from typing import List
from .reel import Reel

class AbstractReelScraper(ABC):
    """
    Абстрактный интерфейс для ingestion-адаптеров (scrapers).
    """
    @abstractmethod
    def fetch_reels_by_hashtag(self, hashtag: str, limit: int = 10) -> List[Reel]:
        """Собирает метаданные рилсов по хэштегу."""
        pass 
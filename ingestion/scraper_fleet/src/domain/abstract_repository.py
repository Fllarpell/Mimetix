from abc import ABC, abstractmethod
from typing import List
from .reel import Reel

class AbstractReelRepository(ABC):
    """
    Абстрактный интерфейс для репозиториев хранения рилсов (S3, GCS, DWH и др.).
    """
    @abstractmethod
    def save(self, reel: Reel) -> None:
        """Сохраняет рилс в хранилище."""
        pass

    @abstractmethod
    def get_all(self) -> List[Reel]:
        """Возвращает все рилсы из хранилища."""
        pass 
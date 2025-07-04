from typing import List
from domain.reel import Reel
from domain.abstract_scraper import AbstractReelScraper

class ScrapyReelScraper(AbstractReelScraper):
    """
    Шаблон ingestion-адаптера для сбора рилсов с помощью Scrapy.
    Наследует интерфейс AbstractReelScraper.

    Рекомендации по реализации:
    - Используйте Scrapy для асинхронного сбора данных с Instagram или других источников.
    - Реализуйте метод fetch_reels_by_hashtag, чтобы возвращать List[Reel].
    - Для хранения сессий, cookies и обхода блокировок используйте middlewares Scrapy.
    - Для unit-тестов мокируйте сетевые запросы.
    - Следуйте best practices: логирование, обработка ошибок, docstring, typing.
    """
    def fetch_reels_by_hashtag(self, hashtag: str, limit: int = 10) -> List[Reel]:
        """
        Собирает метаданные рилсов по хэштегу (реализация через Scrapy).
        Args:
            hashtag: Хэштег без #
            limit: Максимальное количество рилсов
        Returns:
            List[Reel]: Список собранных рилсов
        """
        raise NotImplementedError("Реализация через Scrapy не добавлена. Используйте этот шаблон для расширения.") 
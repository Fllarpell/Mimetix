"""
Entrypoint для Scraper Fleet (ingestion-сервис).
Следует принципам Clean Architecture, SOLID, best practices крупных компаний.
"""
from infrastructure.s3_repository import S3ReelRepository
from infrastructure.gcs_repository import GCSReelRepository
from infrastructure.dwh_repository import DWHReelRepository
from infrastructure.playwright_scraper import PlaywrightReelsScraper
from infrastructure.scrapy_scraper import ScrapyReelScraper
from application.scraper_service import ScraperService
from config import config
import logging
import os
import argparse

# Sentry (ошибки)
try:
    import sentry_sdk
    SENTRY_DSN = config.monitoring.sentry_dsn
    if SENTRY_DSN:
        sentry_sdk.init(dsn=SENTRY_DSN, traces_sample_rate=1.0)
except ImportError:
    pass

# Prometheus (метрики)
try:
    from prometheus_client import start_http_server, Counter
    SCRAPER_SUCCESS = Counter("scraper_success_total", "Number of successful ingestion runs")
    SCRAPER_ERROR = Counter("scraper_error_total", "Number of failed ingestion runs")
    start_http_server(config.monitoring.prometheus_port)
except ImportError:
    SCRAPER_SUCCESS = SCRAPER_ERROR = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("scraper_fleet")

def parse_args():
    parser = argparse.ArgumentParser(description="Scraper Fleet Ingestion Service")
    parser.add_argument("--repository", type=str, default="s3", choices=["s3", "gcs", "dwh"], help="Тип backend-репозитория")
    parser.add_argument("--scraper", type=str, default="playwright", choices=["playwright", "scrapy"], help="Тип скрейпера")
    parser.add_argument("--bucket", type=str, default=config.s3.bucket, help="S3/GCS bucket name")
    parser.add_argument("--prefix", type=str, default=config.s3.prefix, help="S3/GCS prefix")
    parser.add_argument("--dsn", type=str, default=config.dwh.dsn, help="DSN для DWH")
    parser.add_argument("--table", type=str, default=config.dwh.table, help="Таблица для DWH")
    parser.add_argument("--hashtag", type=str, default=config.scraper.hashtag, help="Instagram hashtag")
    parser.add_argument("--limit", type=int, default=config.scraper.limit, help="Reels limit")
    parser.add_argument("--headless", type=lambda x: x.lower() in ("1", "true", "yes"), default=config.scraper.playwright_headless, help="Run browser in headless mode")
    return parser.parse_args()

def get_repository_and_scraper(args):
    # Репозиторий
    if args.repository == "s3":
        repository = S3ReelRepository(bucket=args.bucket, prefix=args.prefix)
    elif args.repository == "gcs":
        repository = GCSReelRepository(bucket=args.bucket, prefix=args.prefix)
    elif args.repository == "dwh":
        repository = DWHReelRepository(dsn=args.dsn, table=args.table)
    else:
        raise ValueError(f"Unknown repository type: {args.repository}")
    # Скрейпер
    if args.scraper == "playwright":
        scraper = PlaywrightReelsScraper(headless=args.headless)
    elif args.scraper == "scrapy":
        scraper = ScrapyReelScraper()
    else:
        raise ValueError(f"Unknown scraper type: {args.scraper}")
    return repository, scraper

def main() -> None:
    """Точка входа для запуска ingestion-сервиса."""
    args = parse_args()
    try:
        repository, scraper = get_repository_and_scraper(args)
        service = ScraperService(repository, scraper)

        logger.info(f"Начинаю сбор рилсов по хэштегу: {args.hashtag}, лимит: {args.limit}")
        reels = service.collect_and_save_reels_by_hashtag(args.hashtag, args.limit)
        logger.info(f"Собрано и сохранено рилсов: {len(reels)}")
        for r in reels:
            logger.debug(r)
        if SCRAPER_SUCCESS:
            SCRAPER_SUCCESS.inc()
    except Exception as e:
        logger.exception(f"Ошибка при запуске ingestion-сервиса: {e}")
        if SCRAPER_ERROR:
            SCRAPER_ERROR.inc()
        # Sentry поймает ошибку автоматически, если инициализирован

if __name__ == "__main__":
    main() 
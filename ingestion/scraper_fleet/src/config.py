"""
Конфиг для Scraper Fleet (ingestion-сервис).
Поддержка ENV, .env-файла (python-dotenv), значения по умолчанию.
"""
from pydantic import BaseSettings, Field, SecretStr
from typing import Optional

class S3Config(BaseSettings):
    bucket: str = Field(..., env="S3_BUCKET")
    prefix: str = Field("reels/", env="S3_PREFIX")
    access_key: Optional[str] = Field(None, env="AWS_ACCESS_KEY_ID")
    secret_key: Optional[SecretStr] = Field(None, env="AWS_SECRET_ACCESS_KEY")
    region: str = Field("us-east-1", env="AWS_DEFAULT_REGION")
    endpoint_url: Optional[str] = Field(None, env="S3_ENDPOINT_URL")

class GCSConfig(BaseSettings):
    bucket: Optional[str] = Field(None, env="GCS_BUCKET")
    prefix: str = Field("reels/", env="GCS_PREFIX")
    credentials_path: Optional[str] = Field(None, env="GOOGLE_APPLICATION_CREDENTIALS")

class DWHConfig(BaseSettings):
    dsn: Optional[str] = Field(None, env="DWH_DSN")
    table: str = Field("reels", env="DWH_TABLE")

class ScraperConfig(BaseSettings):
    hashtag: str = Field("reels", env="HASHTAG")
    limit: int = Field(10, env="REELS_LIMIT")
    playwright_headless: bool = Field(True, env="PLAYWRIGHT_HEADLESS")

class MonitoringConfig(BaseSettings):
    sentry_dsn: Optional[str] = Field(None, env="SENTRY_DSN")
    prometheus_port: int = Field(8000, env="PROMETHEUS_PORT")

class AppConfig(BaseSettings):
    s3: S3Config = S3Config()
    gcs: GCSConfig = GCSConfig()
    dwh: DWHConfig = DWHConfig()
    scraper: ScraperConfig = ScraperConfig()
    monitoring: MonitoringConfig = MonitoringConfig()
    sqlite_path: str = Field("reels.db", env="SQLITE_PATH")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = AppConfig() 
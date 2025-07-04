# Scraper Fleet — Ingestion Service

**Масштабируемый ingestion-сервис для сбора публичных рилсов и метаданных из Instagram и других источников.**

## Архитектурные принципы
- Чистая архитектура (Clean Architecture): разделение на domain, application, infrastructure, interface
- SOLID, SRP, DDD-подходы
- Осмысленные интерфейсы, явные зависимости, тестируемость
- Легко расширять новыми источниками, адаптерами, хранилищами
- Стандарты крупных компаний (Google, SpaceX, Netflix): читаемость, масштабируемость, инженерный минимализм

## Структура
```
scraper_fleet/
  src/
    domain/         # бизнес-логика, сущности, интерфейсы
    application/    # use-cases, сервисы
    infrastructure/ # парсеры, адаптеры, работа с S3/GCS, DWH
    main.py         # entrypoint
  tests/            # тесты (unit, integration)
  README.md         # описание
```

## Минимальный MVP
- Собрать метаданные N публичных рилсов по хэштегу
- Сохранить метаданные в Data Lake (S3/GCS, JSON)
- Легко добавить новые источники/адаптеры (например, для DWH, GCS)

## Best practices
- Type hints, docstrings (Google style)
- Линтеры, тесты, pre-commit
- Нет "магии" и скрытых зависимостей
- README и примеры для каждого слоя
- **Dependency Injection (DI):** выбор backend-ов через фабрику, а не жёстко в main.py

## Хранилище метаданных
- **Data Lake:** AWS S3 или Google Cloud Storage
- **Формат:** JSON (каждый рилс — отдельный объект)
- **Инфраструктурные адаптеры:** S3 (boto3), GCS (google-cloud-storage), расширяемо под DWH (PostgreSQL/ClickHouse)
- **Масштабируемость:** рассчитано на миллионы объектов, production-ready

## Конфигурация через .env

- Пример файла: `.env.example` (скопируйте как `.env` и заполните свои значения)
- Для локального запуска с MinIO или SQLite используйте значения из `.env`
- Для production — заполните переменные для S3, GCS или DWH

**Пример:**
```env
S3_BUCKET=your-s3-bucket
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
S3_ENDPOINT_URL=http://localhost:9000  # для MinIO
HASHTAG=reels
REELS_LIMIT=10
PLAYWRIGHT_HEADLESS=True
```

- Для GCS: укажите GOOGLE_APPLICATION_CREDENTIALS и GCS_BUCKET
- Для DWH: укажите DWH_DSN и DWH_TABLE
- Для SQLite: укажите SQLITE_PATH

**Выбор backend-а:**
- Через CLI: `--repository=s3|gcs|dwh|sqlite`
- Через .env: используйте соответствующие переменные

## Запуск с параметрами ENV, .env и CLI

- Все параметры можно задать через `.env`, переменные окружения или флаги командной строки:
  - `python src/main.py --repository=s3 --scraper=playwright --bucket=my-bucket --hashtag=trends --limit=5 --headless=False`
- Приоритет: CLI > ENV > .env > значения по умолчанию.

## Выбор backend-ов через фабрику (DI)

В main.py реализована фабрика get_repository_and_scraper(args), которая позволяет выбирать backend-репозиторий и скрейпер через CLI/ENV:

```python
repository, scraper = get_repository_and_scraper(args)
service = ScraperService(repository, scraper)
```

Поддерживаются:
- Репозитории: S3, GCS, DWH (PostgreSQL/ClickHouse)
- Скрейперы: Playwright, Scrapy (шаблон)

Добавить новый backend — просто:
1. Реализуйте класс-репозиторий или скрейпер, наследующий абстракцию из domain.
2. Зарегистрируйте его в фабрике get_repository_and_scraper.
3. Добавьте тесты и описание.

## Мониторинг и алерты

- **Sentry**: для мониторинга ошибок, задайте `SENTRY_DSN` в .env/ENV.
- **Prometheus**: метрики доступны на порту `PROMETHEUS_PORT` (по умолчанию 8000).
- Для production используйте секрет-хранилища (Vault, AWS Secrets Manager) для хранения ключей и токенов.

## How to add new data source/storage adapter

1. Создайте новый класс-репозиторий, реализующий интерфейс `AbstractReelRepository` (см. пример GCSReelRepository).
2. Реализуйте методы `save` и `get_all` для нужного хранилища (например, GCS, DWH, локальный диск).
3. Добавьте тесты (unit/integration) для нового адаптера.
4. Зарегистрируйте адаптер в фабрике get_repository_and_scraper в main.py.

## Security best practices

- Все секреты (ключи, токены, пароли) храните только в ENV/.env или секрет-хранилищах (Vault, AWS Secrets Manager, GCP Secret Manager).
- Не коммитьте секреты в git!
- Используйте IAM/Service Accounts с минимальными правами.
- Регулярно меняйте и ротуйте ключи.
- Для production — используйте KMS/Secret Manager, не храните секреты в plain text.

## Observability

- Метрики Prometheus: успешные/ошибочные запуски, latency, бизнес-метрики.
- Алерты: Slack/email через Alertmanager, Airflow, Prefect.
- Логи: используйте structured logging (json-logging) для продакшена.
- Трейсинг: интеграция с OpenTelemetry для end-to-end tracing (опционально).
- В Grafana — дашборды по ingestion, latency, ошибкам.

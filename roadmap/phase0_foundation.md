# Phase 0: Foundation & Data Acquisition

**Goal:** Построить масштабируемую инфраструктуру для сбора, хранения и первичной обработки данных. Это фундамент для всех последующих фаз.

---

## Data Ingestion Fabric — SOTA чеклист (корпоративный уровень)

### 1. Исследование Instagram Graph API
- [ ] 1.1. Найти официальную документацию Instagram Graph API (developer.facebook.com/docs/instagram-api)
- [ ] 1.2. Сохранить ссылку в internal wiki (docs/adr/ingestion_api.md)
- [ ] 1.3. Составить список всех endpoints, связанных с Reels (user media, hashtag search, media insights)
  - [ ] 1.3.1. Для каждого endpoint выписать: URL, метод, параметры, ограничения, пример запроса/ответа
  - [ ] 1.3.2. Сохранить примеры в Postman коллекцию (tools/)
- [ ] 1.4. Выписать ограничения по rate limit для каждого endpoint
  - [ ] 1.4.1. Добавить описание rate limit в ADR (docs/adr/ingestion_api.md)
  - [ ] 1.4.2. Составить стратегию обхода rate limit (backoff, очереди, прокси)
- [ ] 1.5. Проверить, какие поля доступны для Reels (caption, media_url, like_count, comments_count, etc)
  - [ ] 1.5.1. Составить таблицу соответствия полей (docs/data_formats/instagram_reels_fields.md)
  - [ ] 1.5.2. Добавить тестовый ответ API в тестовые данные (tests/data/instagram_reels_sample.json)
- [ ] 1.6. Создать ADR "Выбор стратегии сбора данных" (docs/adr/adr_ingestion_strategy.md)

### 2. Регистрация приложения в Meta/Instagram
- [ ] 2.1. Перейти в Meta for Developers, создать новое приложение
  - [ ] 2.1.1. Сделать скриншоты каждого шага, сохранить в docs/adr/screenshots/
- [ ] 2.2. Добавить Instagram Basic Display/Graph API в приложение
  - [ ] 2.2.1. Документировать настройки (permissions, scopes) в internal wiki
- [ ] 2.3. Получить client_id и client_secret, сохранить в secrets.json
  - [ ] 2.3.1. Добавить client_id/secret в secrets manager (HashiCorp Vault/AWS Secrets Manager)
  - [ ] 2.3.2. Проверить права доступа к секретам (RBAC)
  - [ ] 2.3.3. Добавить тест на отсутствие секретов в git (pre-commit hook)

### 3. Реализация OAuth2 flow
- [ ] 3.1. Реализовать функцию получения authorization code (redirect flow)
  - [ ] 3.1.1. Написать unit-тесты для функции получения кода
  - [ ] 3.1.2. Добавить обработку ошибок (invalid redirect, expired code)
- [ ] 3.2. Реализовать обмен authorization code на access token
  - [ ] 3.2.1. Логировать каждый шаг обмена (info, error)
  - [ ] 3.2.2. Добавить тест на невалидный code
- [ ] 3.3. Сохранить access token в secrets.json, добавить автообновление
  - [ ] 3.3.1. Реализовать refresh token flow
  - [ ] 3.3.2. Добавить алерт на истечение срока действия токена (monitoring/alerting/)
  - [ ] 3.3.3. Проверить traceability токенов (audit log)

### 4. Базовый Python-скрипт для запроса Reels
- [ ] 4.1. Написать функцию get_user_reels(user_id, access_token)
  - [ ] 4.1.1. Описать сигнатуру функции в docs/api/
  - [ ] 4.1.2. Добавить docstring с примерами
- [ ] 4.2. Реализовать пагинацию для получения всех Reels пользователя
  - [ ] 4.2.1. Покрыть пагинацию unit-тестами (edge cases: пустой ответ, конец списка)
- [ ] 4.3. Сохранять каждый ответ API в отдельный raw JSON-файл (data/raw/)
  - [ ] 4.3.1. Проверить atomicity записи (tmp -> rename)
  - [ ] 4.3.2. Добавить тест на race condition при параллельной записи
  - [ ] 4.3.3. Добавить pre-commit на форматирование JSON (prettier)

### 5. Валидация и сохранение метаданных
- [ ] 5.1. Проверить, что все ключевые поля (id, caption, media_url, timestamp) присутствуют в JSON
  - [ ] 5.1.1. Описать схему данных в jsonschema/pydantic
  - [ ] 5.1.2. Добавить тесты на валидацию схемы
- [ ] 5.2. Добавить валидацию схемы JSON (pydantic/jsonschema)
  - [ ] 5.2.1. Логировать ошибки валидации
  - [ ] 5.2.2. Добавить алерт на частые ошибки схемы (monitoring/alerting/)

### 6. Обработка ошибок и логирование
- [ ] 6.1. Добавить try/except для всех запросов к API
  - [ ] 6.1.1. Логировать stacktrace ошибок
  - [ ] 6.1.2. Добавить тесты на обработку ошибок (mock API)
- [ ] 6.2. Логировать ошибки в logs/ingestion_errors.log
  - [ ] 6.2.1. Настроить ротацию логов (logrotate)
  - [ ] 6.2.2. Добавить парсер логов для мониторинга (Promtail/Fluentd)
- [ ] 6.3. Реализовать повторные попытки (retry) при ошибках сети/429
  - [ ] 6.3.1. Использовать экспоненциальный backoff
  - [ ] 6.3.2. Добавить тесты на retry-логику
  - [ ] 6.3.3. Документировать стратегию retry в ADR

### 7. Массовый сбор по списку user_id/hashtag
- [ ] 7.1. Реализовать чтение списка user_id/hashtag из CSV/Google Sheets
  - [ ] 7.1.1. Добавить тестовые CSV/Google Sheets в tests/data/
  - [ ] 7.1.2. Проверить поддержку разных кодировок/разделителей
- [ ] 7.2. Добавить цикл по списку user_id/hashtag для массового сбора
  - [ ] 7.2.1. Логировать прогресс (progress bar, ETA)
  - [ ] 7.2.2. Добавить возможность параллельного сбора (threading/asyncio)
  - [ ] 7.2.3. Добавить тест на race condition при параллельном сборе

### 8. MVP парсера публичных страниц Reels
- [ ] 8.1. Настроить Playwright/Scrapy для парсинга публичных страниц Reels
  - [ ] 8.1.1. Добавить тестовый скрипт для одной страницы
  - [ ] 8.1.2. Документировать структуру HTML-страницы (docs/data_formats/instagram_reels_html.md)
- [ ] 8.2. Реализовать сохранение HTML-дампов и скриншотов Reels
  - [ ] 8.2.1. Проверить atomicity записи HTML/PNG
  - [ ] 8.2.2. Добавить тесты на корректность скриншотов
- [ ] 8.3. Извлекать метаданные (caption, views, likes) из HTML
  - [ ] 8.3.1. Описать парсер как отдельный модуль с unit-тестами
  - [ ] 8.3.2. Добавить тестовые HTML-файлы в tests/data/
  - [ ] 8.3.3. Добавить тесты на edge cases (пустые поля, нестандартная верстка)

### 9. CI/CD, Security, Observability
- [ ] 9.1. Настроить CI pipeline (GitHub Actions/GitLab CI) для запуска тестов ingestion
- [ ] 9.2. Добавить статический анализ кода (flake8, mypy, bandit)
- [ ] 9.3. Проверить отсутствие секретов в истории git (git-secrets)
- [ ] 9.4. Настроить мониторинг доступности API (monitoring/uptime/)
- [ ] 9.5. Добавить trace-id в каждый запрос для трассировки (opentelemetry)
- [ ] 9.6. Документировать все endpoints и параметры в docs/api/
- [ ] 9.7. Провести code review по чеклисту безопасности
- [ ] 9.8. Провести нагрузочное тестирование ingestion (tools/loadtest/)
- [ ] 9.9. Добавить алерты на превышение rate limit, ошибки 5xx, падение скорости сбора

---

## Data Lakehouse (детализация)
- [ ] 10.1. Создать бакет S3/MinIO для raw/bronze/silver/gold
  - [ ] 10.1.1. Описать структуру бакета в docs/data_formats/storage_layout.md
  - [ ] 10.1.2. Настроить versioning и lifecycle policy
- [ ] 10.2. Настроить IAM/policy для доступа
  - [ ] 10.2.1. Проверить least privilege для сервисных аккаунтов
  - [ ] 10.2.2. Добавить тест на доступность бакета из CI
- [ ] 10.3. Реализовать upload/download тестовые скрипты
  - [ ] 10.3.1. Добавить unit-тесты на upload/download
  - [ ] 10.3.2. Проверить atomicity операций

---

## ETL/ELT Pipelines (детализация)
- [ ] 11.1. Создать Airflow DAG для ежедневного сбора
  - [ ] 11.1.1. Описать DAG в docs/architecture/airflow_dags.md
  - [ ] 11.1.2. Добавить тестовый DAG для mock данных
- [ ] 11.2. Написать Python-скрипт для очистки и нормализации
  - [ ] 11.2.1. Добавить unit-тесты для функций очистки
  - [ ] 11.2.2. Документировать pipeline в docs/data_formats/etl_flow.md

---

## Initial EDA & Metrics (детализация)
- [ ] 12.1. Создать Jupyter-ноутбук для анализа метаданных
  - [ ] 12.1.1. Добавить тестовые данные для ноутбука
  - [ ] 12.1.2. Описать структуру ноутбука в docs/architecture/eda_template.md
- [ ] 12.2. Построить графики распределения просмотров, ER, времени публикации
  - [ ] 12.2.1. Добавить unit-тесты для функций построения графиков
  - [ ] 12.2.2. Сохранить графики в reports/eda/
- [ ] 12.3. Провести peer review ноутбука (pull request)

---

## Deliverables
- Автоматизированный сбор данных (10k+ Reels/день)
- Data Lake с raw/bronze/silver/gold слоями
- Первый EDA-отчет, формализация метрики виральности
- Документированные ADR по архитектуре ingestion/storage

---

## Links
- [../roadmap.md](../roadmap.md)
- [PHASES.md](./PHASES.md)
- [../plan.md](../plan.md) 
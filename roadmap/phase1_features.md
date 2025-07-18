# Phase 1: Multi-Modal Feature Extraction

**Goal:** Автоматически извлекать структурированные признаки из видео, аудио и текста для ML/аналитики, с оптимизацией хранения и массовым анализом по метаданным.

---

## Feature Extraction — SOTA чеклист (корпоративный уровень)

### 1. Подготовка данных
- [ ] 1.1. Проверить наличие raw видео/аудио файлов в data/raw/
  - [ ] 1.1.1. Добавить тестовые видео/аудио в tests/data/
  - [ ] 1.1.2. Проверить права доступа к data/raw/ (RBAC)
- [ ] 1.2. Составить список файлов для обработки (csv/json)
  - [ ] 1.2.1. Добавить unit-тест на чтение списка файлов
  - [ ] 1.2.2. Проверить поддержку разных форматов (csv, json, parquet)
- [ ] 1.3. Описать структуру входных данных в docs/data_formats/feature_input.md
- [ ] 1.4. Создать ADR "Стандарты хранения и именования raw данных" (docs/adr/adr_raw_data_naming.md)

### 2. Установка зависимостей и окружения
- [ ] 2.1. Установить ffmpeg, tesseract, pytorch, torchvision, transformers, whisper, easyocr, mediapipe, librosa
  - [ ] 2.1.1. Описать зависимости в requirements.txt/conda.yaml
  - [ ] 2.1.2. Добавить pre-commit на проверку зависимостей
- [ ] 2.2. Проверить доступность GPU (nvidia-smi)
  - [ ] 2.2.1. Добавить тест на автоматическую проверку GPU
- [ ] 2.3. Настроить Dockerfile для пайплайна extraction
  - [ ] 2.3.1. Добавить CI для сборки Docker-образа
- [ ] 2.4. Описать окружение в docs/development/env_setup.md

### 3. Видеофичи (Visual)
- [ ] 3.1. Реализовать извлечение длительности, fps, разрешения (ffprobe)
  - [ ] 3.1.1. Добавить unit-тесты для каждого параметра
  - [ ] 3.1.2. Логировать ошибки извлечения
- [ ] 3.2. Реализовать scene detection (PySceneDetect)
  - [ ] 3.2.1. Добавить тестовые видео с разным количеством сцен
  - [ ] 3.2.2. Сохранить результаты в feature_store/interim/visual/
- [ ] 3.3. Реализовать OCR (EasyOCR/PaddleOCR) для извлечения текста
  - [ ] 3.3.1. Добавить тестовые видео с текстом/без текста
  - [ ] 3.3.2. Сохранить результаты OCR в отдельный json
- [ ] 3.4. Реализовать object/face detection (YOLO/MediaPipe)
  - [ ] 3.4.1. Добавить unit-тесты на разные типы объектов
  - [ ] 3.4.2. Сохранить bounding boxes в feature_store/interim/visual/
- [ ] 3.5. Получить CLIP-эмбеддинги для каждого видео (OpenAI CLIP)
  - [ ] 3.5.1. Добавить тест на корректность размерности эмбеддинга
  - [ ] 3.5.2. Сохранить эмбеддинги в vector_db
- [ ] 3.6. Добавить логирование времени обработки каждого видео
- [ ] 3.7. Описать схему визуальных признаков в docs/data_formats/visual_features.md
- [ ] 3.8. Добавить тесты на data drift визуальных признаков

### 4. Аудиофичи (Audio)
- [ ] 4.1. Извлечь аудиодорожку из видео (ffmpeg)
  - [ ] 4.1.1. Добавить тесты на разные форматы видео
- [ ] 4.2. Реализовать Whisper STT для транскрипции
  - [ ] 4.2.1. Добавить тестовые аудио с разной речью/языками
  - [ ] 4.2.2. Сохранить транскрипции в feature_store/interim/audio/
- [ ] 4.3. Реализовать audio fingerprinting (dejavu/acrcloud)
  - [ ] 4.3.1. Добавить тесты на совпадение/различие фингерпринтов
- [ ] 4.4. Определить BPM, loudness (librosa)
  - [ ] 4.4.1. Добавить тесты на разные жанры музыки
- [ ] 4.5. Разделить речь/музыку (VAD)
  - [ ] 4.5.1. Добавить тесты на edge cases (шум, тишина)
- [ ] 4.6. Сохранить все аудиопризнаки в feature_store/interim/audio/
- [ ] 4.7. Описать схему аудиопризнаков в docs/data_formats/audio_features.md
- [ ] 4.8. Добавить тесты на data drift аудиопризнаков

### 5. Текстовые фичи (NLP)
- [ ] 5.1. Обработать description и транскрипцию
  - [ ] 5.1.1. Добавить тестовые описания (разные языки, длина, эмодзи)
- [ ] 5.2. Провести topic modeling (BERTopic/LDA)
  - [ ] 5.2.1. Добавить тесты на разные темы
- [ ] 5.3. Анализ тональности (sentiment, transformers)
  - [ ] 5.3.1. Добавить тесты на позитив/негатив/нейтрал
- [ ] 5.4. NER (spaCy)
  - [ ] 5.4.1. Добавить тесты на извлечение именованных сущностей
- [ ] 5.5. Получить BERT/LLM-эмбеддинги
  - [ ] 5.5.1. Добавить тест на размерность эмбеддинга
- [ ] 5.6. Сохранить все текстовые признаки в feature_store/interim/text/
- [ ] 5.7. Описать схему текстовых признаков в docs/data_formats/text_features.md
- [ ] 5.8. Добавить тесты на data drift текстовых признаков

### 6. Feature Store
- [ ] 6.1. Настроить Feast/Tecton
  - [ ] 6.1.1. Описать структуру feature store в docs/data_formats/feature_store_layout.md
  - [ ] 6.1.2. Добавить тесты на загрузку/выгрузку признаков
- [ ] 6.2. Версионировать признаки (data lineage)
  - [ ] 6.2.1. Добавить data contract для каждого типа признаков
  - [ ] 6.2.2. Добавить тесты на совместимость версий
- [ ] 6.3. Добавить мониторинг качества признаков (data quality)
  - [ ] 6.3.1. Настроить алерты на пропуски, аномалии, outliers
- [ ] 6.4. Добавить trace-id для каждого набора признаков
- [ ] 6.5. Провести code review схемы признаков

### 7. Pipeline Orchestration
- [ ] 7.1. Создать Airflow DAG для автоматизации feature extraction
  - [ ] 7.1.1. Описать DAG в docs/architecture/airflow_dags.md
  - [ ] 7.1.2. Добавить тестовый DAG для mock данных
- [ ] 7.2. Логировать все ошибки пайплайнов
  - [ ] 7.2.1. Настроить ротацию логов
  - [ ] 7.2.2. Добавить парсер логов для мониторинга (Promtail/Fluentd)
- [ ] 7.3. Добавить алерты на сбои пайплайнов (monitoring/alerting/)
- [ ] 7.4. Добавить тесты на idempotency пайплайна
- [ ] 7.5. Добавить возможность ручного запуска пайплайна (trigger)

### 8. Документация, тесты, observability, security
- [ ] 8.1. Описать схемы признаков в docs/data_formats/
- [ ] 8.2. Добавить unit-тесты для каждого экстрактора (visual, audio, text)
- [ ] 8.3. Протестировать пайплайн на 10+ видео/аудио/текстах
- [ ] 8.4. Добавить статический анализ кода (flake8, mypy, bandit)
- [ ] 8.5. Настроить CI pipeline для запуска тестов extraction
- [ ] 8.6. Проверить отсутствие секретов в git (git-secrets)
- [ ] 8.7. Провести code review по чеклисту безопасности
- [ ] 8.8. Добавить traceability для всех артефактов extraction
- [ ] 8.9. Провести нагрузочное тестирование extraction (tools/loadtest/)
- [ ] 8.10. Провести peer review пайплайна (pull request)
- [ ] 8.11. Добавить A/B тесты для новых признаков

---

## Оптимизация feature extraction (новое)
- Основной поток — обработка и анализ метаданных (описание, лайки, просмотры, хэштеги, дата, автор).
- Видео и аудио скачиваются и анализируются только для топ-N рилсов (по просмотрам, лайкам, ER и др.).
- Пайплайны должны быть устойчивы к отсутствию видео/аудио (если рилс не попал в топ-N — анализ только по метаданным).
- Хранение видео — только для топ-N, остальные данные — в виде метаданных.

---

## Deliverables
- Feature Store с multi-modal векторами, оптимизированный под частичное отсутствие видео/аудио (массовый анализ по метаданным, deep dive по топ-N).
- Автоматические пайплайны для извлечения признаков
- Jupyter-ноутбуки с анализом важности признаков

---

## Links
- [../roadmap.md](../roadmap.md)
- [PHASES.md](./PHASES.md)
- [../plan.md](../plan.md) 
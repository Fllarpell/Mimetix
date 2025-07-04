# Phase 2: Predictive Modeling & Trend Detection

**Goal:** Построить ML-модели для предсказания виральности и автоматической детекции трендов.

---

## Predictive Modeling & Trend Detection — SOTA чеклист (корпоративный уровень)

### 1. Подготовка данных и EDA
- [ ] 1.1. Сформировать датасет признаков из Feature Store (feature_store/feast/)
  - [ ] 1.1.1. Добавить unit-тесты на корректность выгрузки
  - [ ] 1.1.2. Проверить data lineage для каждого признака
- [ ] 1.2. Провести EDA (Jupyter/Databricks)
  - [ ] 1.2.1. Построить графики распределения целевой переменной (virality_score)
  - [ ] 1.2.2. Проверить пропуски, выбросы, аномалии
  - [ ] 1.2.3. Сохранить EDA-отчет в reports/eda/
- [ ] 1.3. Описать структуру датасета в docs/data_formats/model_input.md
- [ ] 1.4. Создать ADR "Стандарты подготовки данных для ML" (docs/adr/adr_ml_data_prep.md)

### 2. Baseline и Feature Engineering
- [ ] 2.1. Реализовать baseline-модель (логистическая регрессия/решающее дерево)
  - [ ] 2.1.1. Добавить unit-тесты для baseline
  - [ ] 2.1.2. Сохранить baseline-метрики (accuracy, ROC-AUC, F1)
- [ ] 2.2. Провести feature engineering (feature selection, scaling, encoding)
  - [ ] 2.2.1. Добавить тесты на корректность трансформаций
  - [ ] 2.2.2. Описать pipeline feature engineering в docs/data_formats/feature_eng_pipeline.md
- [ ] 2.3. Добавить data contract для входных признаков (pydantic/jsonschema)
  - [ ] 2.3.1. Добавить тесты на совместимость версий признаков
- [ ] 2.4. Добавить мониторинг data drift (evidently, whylogs)
  - [ ] 2.4.1. Настроить алерты на drift

### 3. ML pipeline (SOTA)
- [ ] 3.1. Реализовать ML pipeline (sklearn/pipeline, MLflow)
  - [ ] 3.1.1. Добавить unit-тесты для каждого шага pipeline
  - [ ] 3.1.2. Описать pipeline в docs/architecture/ml_pipeline.md
- [ ] 3.2. Реализовать трекинг экспериментов (MLflow/W&B)
  - [ ] 3.2.1. Добавить автоматическую запись параметров, метрик, артефактов
  - [ ] 3.2.2. Проверить reproducibility экспериментов
- [ ] 3.3. Реализовать автоматический подбор гиперпараметров (Optuna, W&B Sweeps)
  - [ ] 3.3.1. Добавить тесты на корректность поиска
- [ ] 3.4. Добавить explainability (SHAP, LIME)
  - [ ] 3.4.1. Сохранить отчеты explainability в reports/explain/
  - [ ] 3.4.2. Добавить unit-тесты для explainability функций
- [ ] 3.5. Добавить A/B тесты для новых моделей
- [ ] 3.6. Добавить мониторинг качества модели (model drift, performance)
  - [ ] 3.6.1. Настроить алерты на падение метрик
- [ ] 3.7. Добавить trace-id для каждого инференса
- [ ] 3.8. Провести code review pipeline по чеклисту безопасности

### 4. Trend Detection Engine
- [ ] 4.1. Реализовать time series anomaly detection (Prophet, ARIMA, S-H-ESD)
  - [ ] 4.1.1. Добавить тесты на synthetic data
  - [ ] 4.1.2. Описать pipeline в docs/architecture/trend_detection.md
- [ ] 4.2. Реализовать кластеризацию аудио/визуальных признаков (DBSCAN/HDBSCAN)
  - [ ] 4.2.1. Добавить тесты на корректность кластеризации
- [ ] 4.3. Реализовать графовый анализ трендов (Neo4j, GNNs)
  - [ ] 4.3.1. Добавить тесты на community detection
  - [ ] 4.3.2. Описать схему графа в docs/data_formats/trend_graph.md
- [ ] 4.4. Добавить explainability для трендов (LLM summary, feature importance)
- [ ] 4.5. Добавить мониторинг drift трендов
- [ ] 4.6. Добавить traceability для всех найденных трендов

### 5. Causal Inference
- [ ] 5.1. Реализовать causal inference pipeline (EconML, DoWhy, CEVAE)
  - [ ] 5.1.1. Добавить тесты на synthetic data
  - [ ] 5.1.2. Сохранить отчеты по каузальному анализу в reports/causal/
- [ ] 5.2. Добавить explainability для каузальных выводов
- [ ] 5.3. Добавить monitoring/alerting на ошибки inference

### 6. Vector Search & Semantic API
- [ ] 6.1. Настроить vector DB (Pinecone/Weaviate)
  - [ ] 6.1.1. Добавить тесты на insert/search
  - [ ] 6.1.2. Описать схему индексации в docs/data_formats/vector_index.md
- [ ] 6.2. Реализовать API поиска (FastAPI, gRPC)
  - [ ] 6.2.1. Добавить unit/integration тесты для API
  - [ ] 6.2.2. Добавить trace-id для каждого запроса
- [ ] 6.3. Добавить monitoring/alerting на latency, ошибки поиска

### 7. CI/CD, Security, Observability
- [ ] 7.1. Настроить CI pipeline (GitHub Actions/GitLab CI) для запуска тестов ML/Trend
- [ ] 7.2. Добавить статический анализ кода (flake8, mypy, bandit)
- [ ] 7.3. Проверить отсутствие секретов в истории git (git-secrets)
- [ ] 7.4. Настроить мониторинг качества данных и моделей (Prometheus, Grafana, Evidently)
- [ ] 7.5. Добавить traceability для всех артефактов pipeline
- [ ] 7.6. Провести code review по чеклисту безопасности
- [ ] 7.7. Провести нагрузочное тестирование inference (tools/loadtest/)
- [ ] 7.8. Провести peer review pipeline (pull request)

### 8. Документация, reproducibility, peer review
- [ ] 8.1. Описать все pipeline, схемы, контракты в docs/architecture/ и docs/data_formats/
- [ ] 8.2. Добавить примеры запуска pipeline (README, notebooks)
- [ ] 8.3. Добавить unit/integration тесты для всех компонентов
- [ ] 8.4. Проверить reproducibility pipeline (seed, random_state)
- [ ] 8.5. Провести peer review документации

---

## Deliverables
- Модель предсказания виральности (регрессия/классификация)
- Автоматическая детекция трендов (аудио, визуальные, мемы)
- Отчеты по каузальному анализу
- API семантического поиска

---

## Links
- [../roadmap.md](../roadmap.md)
- [PHASES.md](./PHASES.md)
- [../plan.md](../plan.md) 
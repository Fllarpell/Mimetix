# Phase 4: Generative AI & Creative Co-Pilot

**Goal:** Построить AI-ассистента для генерации сценариев и идей, учитывающего ограничения по доступности видео/аудио, с массовым анализом по метаданным и deep dive по топ-N рилсам.

---

## Generative AI & Co-Pilot — SOTA чеклист (корпоративный уровень)

### 1. Проектирование архитектуры Generative Co-Pilot
- [ ] 1.1. Описать архитектуру LLM+RAG (docs/architecture/generative_copilot.md)
  - [ ] 1.1.1. Создать ADR "Архитектура генеративного ассистента" (docs/adr/adr_generative_arch.md)
  - [ ] 1.1.2. Описать data flow: input → retrieval → LLM → output
- [ ] 1.2. Описать требования к latency, quality, explainability, observability
- [ ] 1.3. Описать схемы входных/выходных данных (docs/data_formats/generative_input_output.md)
- [ ] 1.4. Добавить data contract для prompt/response (pydantic/jsonschema)

### 2. Интеграция с трендами и аналитикой
- [ ] 2.1. Реализовать интеграцию с Trend Engine (API, vector search)
  - [ ] 2.1.1. Добавить unit/integration тесты для интеграции
  - [ ] 2.1.2. Добавить trace-id для всех запросов к трендам
- [ ] 2.2. Реализовать retrieval-augmented generation (RAG)
  - [ ] 2.2.1. Добавить тесты на релевантность retrieved контекста
  - [ ] 2.2.2. Описать pipeline RAG в docs/architecture/rag_pipeline.md
- [ ] 2.3. Добавить monitoring/alerting на ошибки интеграции

### 3. Промпт-инжиниринг и генерация сценариев
- [ ] 3.1. Описать стандарты промптов (llm_prompts/README.md)
  - [ ] 3.1.1. Добавить ADR "Стандарты промпт-инжиниринга" (docs/adr/adr_prompt_standards.md)
- [ ] 3.2. Реализовать генерацию сценариев (LLM, OpenAI, Llama, Mistral)
  - [ ] 3.2.1. Добавить unit/integration тесты генерации
  - [ ] 3.2.2. Добавить тесты на корректность структуры сценария
  - [ ] 3.2.3. Добавить A/B тесты для новых промптов/моделей
- [ ] 3.3. Реализовать оптимизационный цикл (RLHF, RLAIF, genetic search)
  - [ ] 3.3.1. Добавить тесты на convergence/quality
- [ ] 3.4. Добавить explainability для генерации (LLM output rationale)
- [ ] 3.5. Добавить monitoring/alerting на ошибки генерации

### 4. API и User-Facing Apps
- [ ] 4.1. Проектировать OpenAPI/gRPC спецификацию для генеративных endpoints (docs/api/)
  - [ ] 4.1.1. Описать все endpoints, параметры, типы ошибок, версии
  - [ ] 4.1.2. Добавить примеры запросов/ответов (Postman, Swagger)
- [ ] 4.2. Реализовать backend API для генерации (FastAPI/Go)
  - [ ] 4.2.1. Добавить unit/integration тесты для каждого endpoint
  - [ ] 4.2.2. Добавить обработку ошибок, валидацию входных данных
  - [ ] 4.2.3. Добавить логирование запросов/ответов (trace-id, user-id)
  - [ ] 4.2.4. Добавить версионирование API
- [ ] 4.3. Реализовать user-facing app (user_apps/script_generator/)
  - [ ] 4.3.1. Добавить unit/integration/e2e тесты для UI
  - [ ] 4.3.2. Добавить accessibility тесты (a11y)
  - [ ] 4.3.3. Добавить UX-тесты с креаторами
- [ ] 4.4. Настроить CI/CD pipeline для генеративных сервисов
  - [ ] 4.4.1. Добавить статический анализ кода (flake8, mypy, bandit, eslint)
  - [ ] 4.4.2. Проверить отсутствие секретов в git
  - [ ] 4.4.3. Добавить автоматический деплой на staging
- [ ] 4.5. Настроить observability (Prometheus, Grafana, Sentry)
  - [ ] 4.5.1. Добавить метрики latency, error rate, throughput, quality
  - [ ] 4.5.2. Добавить trace-id для всех запросов
  - [ ] 4.5.3. Настроить алерты на ошибки, деградацию качества
- [ ] 4.6. Провести нагрузочное тестирование генеративных endpoints
- [ ] 4.7. Провести code review по чеклисту безопасности
- [ ] 4.8. Провести peer review API и UI (pull request)

### 5. Prompt evaluation, explainability, peer review
- [ ] 5.1. Реализовать автоматическую оценку качества генерации (BLEU, ROUGE, human eval)
  - [ ] 5.1.1. Добавить тесты на корректность метрик
  - [ ] 5.1.2. Добавить human-in-the-loop для оценки сценариев
- [ ] 5.2. Добавить explainability для LLM output (attention, rationale)
- [ ] 5.3. Добавить traceability для всех промптов и ответов
- [ ] 5.4. Описать все схемы, пайплайны, стандарты в docs/architecture/, docs/data_formats/, llm_prompts/
- [ ] 5.5. Провести peer review документации и пайплайнов

---

## Оптимизация генеративной фазы (новое)
- Генерация сценариев и рекомендации строятся преимущественно на трендах и аналитике, полученных из метаданных.
- Deep dive и генерация по видео/аудио — только для топ-N рилсов.
- В RAG — контекст формируется из наиболее релевантных метаданных и видео топ-N рилсов.

---

## Deliverables
- AI-powered генератор сценариев и ассистент, учитывающий ограничения по доступности видео/аудио (массовый анализ по метаданным, deep dive по топ-N).
- Инструменты для креаторов

---

## Links
- [../roadmap.md](../roadmap.md)
- [PHASES.md](./PHASES.md)
- [../plan.md](../plan.md) 
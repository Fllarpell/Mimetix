# Phase 3: Productization & Delivery

**Goal:** Доставить инсайты и рекомендации через API и дашборды. Обеспечить MLOps, документацию, мониторинг.

---

## Productization & Delivery — SOTA чеклист (корпоративный уровень)

### 1. Проектирование и реализация Backend API
- [ ] 1.1. Проектировать OpenAPI/GraphQL спецификацию (docs/api/)
  - [ ] 1.1.1. Описать все endpoints, параметры, типы ошибок, версии
  - [ ] 1.1.2. Добавить примеры запросов/ответов (Postman, Swagger)
  - [ ] 1.1.3. Создать ADR "Стандарты API" (docs/adr/adr_api_standards.md)
- [ ] 1.2. Реализовать backend API (FastAPI/Go/Node.js)
  - [ ] 1.2.1. Добавить unit/integration тесты для каждого endpoint
  - [ ] 1.2.2. Добавить обработку ошибок, валидацию входных данных
  - [ ] 1.2.3. Добавить логирование запросов/ответов (trace-id, user-id)
  - [ ] 1.2.4. Добавить версионирование API (v1, v2)
  - [ ] 1.2.5. Добавить тесты на backward compatibility
- [ ] 1.3. Реализовать gRPC endpoints для внутренних сервисов
  - [ ] 1.3.1. Описать protobuf схемы (api/protos/)
  - [ ] 1.3.2. Добавить unit/integration тесты для gRPC
- [ ] 1.4. Настроить CI/CD pipeline для backend (GitHub Actions/GitLab CI)
  - [ ] 1.4.1. Добавить статический анализ кода (flake8, mypy, bandit, gosec)
  - [ ] 1.4.2. Проверить отсутствие секретов в git (git-secrets)
  - [ ] 1.4.3. Добавить автоматический деплой на staging
- [ ] 1.5. Настроить observability (Prometheus, Grafana, Jaeger)
  - [ ] 1.5.1. Добавить метрики latency, error rate, throughput
  - [ ] 1.5.2. Добавить trace-id для всех запросов
  - [ ] 1.5.3. Настроить алерты на ошибки 5xx, деградацию SLA
- [ ] 1.6. Провести нагрузочное тестирование API (tools/loadtest/)
- [ ] 1.7. Провести code review по чеклисту безопасности
- [ ] 1.8. Провести peer review API (pull request)

### 2. Frontend Dashboard (Trend Radar, Explainable Analytics)
- [ ] 2.1. Проектировать UX/UI (Figma, Miro)
  - [ ] 2.1.1. Описать user stories, сценарии, прототипы
  - [ ] 2.1.2. Провести UX-тестирование прототипа
  - [ ] 2.1.3. Создать ADR "Стандарты UX/UI" (docs/adr/adr_ux_standards.md)
- [ ] 2.2. Реализовать frontend (React/Vue/Svelte)
  - [ ] 2.2.1. Добавить unit/integration тесты для компонентов
  - [ ] 2.2.2. Добавить e2e тесты (Cypress, Playwright)
  - [ ] 2.2.3. Добавить accessibility тесты (a11y)
  - [ ] 2.2.4. Добавить логирование действий пользователя (analytics)
  - [ ] 2.2.5. Добавить версионирование frontend
- [ ] 2.3. Настроить CI/CD pipeline для frontend
  - [ ] 2.3.1. Добавить статический анализ кода (eslint, stylelint)
  - [ ] 2.3.2. Проверить отсутствие секретов в git
  - [ ] 2.3.3. Добавить автоматический деплой на staging
- [ ] 2.4. Настроить observability (Sentry, Grafana)
  - [ ] 2.4.1. Добавить метрики загрузки, ошибок, пользовательских событий
  - [ ] 2.4.2. Настроить алерты на деградацию UX
- [ ] 2.5. Провести нагрузочное тестирование frontend
- [ ] 2.6. Провести code review по чеклисту безопасности
- [ ] 2.7. Провести peer review frontend (pull request)

### 3. MLOps & CI/CD
- [ ] 3.1. Настроить автоматический retraining моделей (Airflow, Jenkins, GitLab CI)
  - [ ] 3.1.1. Добавить тесты на корректность retraining pipeline
  - [ ] 3.1.2. Добавить алерты на сбои retraining
- [ ] 3.2. Настроить автоматический деплой моделей (MLflow, Seldon, Triton)
  - [ ] 3.2.1. Добавить тесты на корректность деплоя
  - [ ] 3.2.2. Добавить мониторинг latency, accuracy, drift
- [ ] 3.3. Настроить мониторинг пайплайнов (Prometheus, Grafana, Evidently)
  - [ ] 3.3.1. Добавить алерты на сбои пайплайнов
  - [ ] 3.3.2. Добавить traceability для всех артефактов
- [ ] 3.4. Провести code review по чеклисту безопасности MLOps
- [ ] 3.5. Провести peer review MLOps pipeline

### 4. Документация, SLA/SLO, peer review
- [ ] 4.1. Описать все API, схемы, пайплайны, UX в docs/api/, docs/architecture/, docs/data_formats/
- [ ] 4.2. Добавить примеры использования API (README, Postman)
- [ ] 4.3. Описать SLA/SLO для всех сервисов (docs/architecture/sla_slo.md)
- [ ] 4.4. Добавить unit/integration/e2e тесты для всех компонентов
- [ ] 4.5. Проверить traceability и data lineage для всех артефактов
- [ ] 4.6. Провести peer review документации

---

## Deliverables
- Публичный API для анализа, трендов, рекомендаций
- Интерактивный дашборд
- Автоматизация retraining и мониторинга

---

## Links
- [../roadmap.md](../roadmap.md)
- [PHASES.md](./PHASES.md)
- [../plan.md](../plan.md) 
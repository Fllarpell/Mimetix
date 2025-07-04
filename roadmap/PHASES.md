# Roadmap Phases Overview

Этот файл — навигация по основным фазам реализации SOTA Reels Intelligence Platform. Для каждой фазы есть отдельный подробный roadmap/README.

---

## Phase 0: Foundation & Data Acquisition
- [phase0_foundation.md](./phase0_foundation.md)
- Цель: Инфраструктура гибридного сбора (API + web scraping), массовый сбор и хранение метаданных, фильтрация топ-N рилсов для скачивания видео, оптимизация хранения, устойчивость к блокировкам.
- Deliverables: Масштабируемый гибридный сбор, автоматизация, Data Lake, первый EDA-отчет.

## Phase 1: Multi-Modal Feature Extraction
- [phase1_features.md](./phase1_features.md)
- Цель: Извлечение признаков из видео/аудио только для топ-N рилсов, массовый анализ по метаданным, устойчивость к отсутствию видео, оптимизация хранения.
- Deliverables: Автоматические пайплайны, Feature Store, анализ важности признаков.

## Phase 2: Predictive Modeling & Trend Detection
- [phase2_modeling.md](./phase2_modeling.md)
- Цель: Модели предсказания виральности и тренд-детекции, устойчивые к частичному отсутствию видео/аудио, массовый анализ по метаданным, deep dive по топ-N.
- Deliverables: Модели и пайплайны, устойчивые к неполным данным, автоматическая детекция трендов, API поиска.

## Phase 3: Productization & Delivery
- [phase3_product.md](./phase3_product.md)
- Цель: API и дашборды, устойчивые к неполному сбору данных, массовый анализ по метаданным, deep dive по топ-N, мониторинг устойчивости пайплайнов.
- Deliverables: Публичный API, дашборд, автоматизация retraining.

## Phase 4: Generative AI & Co-Pilot
- [phase4_generative.md](./phase4_generative.md)
- Цель: Генеративный AI-ассистент, работающий преимущественно с метаданными, deep dive по топ-N, устойчивость к отсутствию видео/аудио.
- Deliverables: Генератор сценариев, ассистент, инструменты для креаторов.

---

## Cross-Cutting Concerns
- Security, Compliance, Data Governance, R&D, Team

---

## См. также
- [../roadmap.md](../roadmap.md) — полный roadmap
- [../README.md](../README.md) — обзор проекта
- [../docs/architecture/](../docs/architecture/) — архитектура и схемы 
# Project Prometheus — SOTA Roadmap

> This roadmap is a living document. Each phase links to relevant directories and documentation in the monorepo.

---

## Phase 0: Foundation & Data Acquisition (1-2 months)
**Goal:** Build robust, scalable infrastructure for hybrid data collection (API + web scraping) and storage. Lay the foundation for all future analytics and ML. Mass ingestion of metadata, video download only for top-N reels, storage optimization, resilience to blocking.

### Key Tasks
- **Data Ingestion Fabric**
  - [ingestion/scraper_fleet/](./ingestion/scraper_fleet/): Scrapy/Playwright, proxy management, hybrid flow (API + scraping)
  - [ingestion/api_connectors/](./ingestion/api_connectors/): Instagram Graph API, partner integrations
  - [ingestion/firehose/](./ingestion/firehose/): Real-time data subscriptions
  - Filter top-N reels for video download, collect only metadata for the rest
  - Implement task queues, proxy pool, user-agent randomization, delays, error logging, retry
- **Data Lakehouse**
  - [storage/lakehouse/](./storage/lakehouse/): S3/GCS, Delta Lake, Hudi
- **ETL/ELT Pipelines**
  - [orchestration/airflow/](./orchestration/airflow/): Airflow DAGs for batch jobs
  - [data_pipelines/](./data_pipelines/): Python ETL scripts
- **Initial EDA & Metrics**
  - [research/notebooks/](./research/notebooks/): Jupyter, Pandas, EDA
  - [docs/adr/](./docs/adr/): Document key decisions

**Deliverables:**
- Scalable hybrid ingestion (API + scraping), mass metadata collection, video download only for top-N, storage optimization, resilience to blocking, automated retry
- Automated data ingestion (10k+ Reels/day)
- Data Lake with raw/bronze/silver/gold layers
- First EDA report, virality metric formalized

---

## Phase 1: Multi-Modal Feature Extraction (2-3 months)
**Goal:** Extract structured, ML-ready features from video, audio, and text. Video/audio processing only for top-N reels, mass analysis on metadata, storage optimization, resilience to missing video/audio.

### Key Tasks
- **Video Processing**
  - [services/feature_extractor_visual/](./services/feature_extractor_visual/): Scene detection, OCR, object/face detection, CLIP embeddings (only for top-N reels)
- **Audio Processing**
  - [services/feature_extractor_audio/](./services/feature_extractor_audio/): Whisper STT, audio fingerprinting, BPM, music/speech split (only for top-N reels)
- **Text/NLP**
  - [services/event_consumer/](./services/event_consumer/): Description, transcript, topic modeling, sentiment, NER (for all reels)
- **Feature Store**
  - [feature_store/feast/](./feature_store/feast/): Centralized feature storage
- **Pipeline Orchestration**
  - [orchestration/airflow/](./orchestration/airflow/): Automated feature extraction

**Deliverables:**
- Feature Store with multi-modal vectors, optimized for partial absence of video/audio (mass analysis on metadata, deep dive for top-N)
- Automated pipelines for feature extraction
- Notebooks with feature importance analysis

---

## Phase 2: Predictive Modeling & Trend Detection (2-3 months)
**Goal:** Build models to predict virality and detect trends in real time. Datasets are mostly metadata, deep analysis (visual/audio) only for top-N. Models must handle incomplete data.

### Key Tasks
- **Predictive Modeling**
  - [ml/](./ml/): XGBoost, LightGBM, CatBoost, PyTorch, MLflow tracking
  - [model_registry/mlflow/](./model_registry/mlflow/): Model registry
- **Trend Detection Engine**
  - [intelligence/trend_engine/](./intelligence/trend_engine/): Time series anomaly detection, graph analytics (mass analysis on metadata, deep dive for top-N)
  - [storage/timeseries_db/](./storage/timeseries_db/): ClickHouse, TimescaleDB
  - [storage/graph_db/](./storage/graph_db/): Neo4j, GNNs
- **Causal Inference**
  - [intelligence/causal_engine/](./intelligence/causal_engine/): SHAP, LIME, CEVAE, Dragonnet
- **Vector Search**
  - [storage/vector_db/](./storage/vector_db/): Pinecone, Weaviate

**Deliverables:**
- Models and pipelines resilient to partial absence of video/audio (mass analysis on metadata, deep dive for top-N)
- Virality prediction model (regression/classification)
- Automated trend detection (audio, visual, meme)
- Causal analysis reports
- Semantic search API

---

## Phase 3: Productization & Delivery (2-4 months)
**Goal:** Deliver insights and recommendations via API and dashboards. API and dashboard must support both full data (metadata+video) and metadata-only. Trend visualization — on metadata, deep dive for top-N. MLOps — monitor pipeline resilience to blocking.

### Key Tasks
- **Backend API**
  - [api_gateway/](./api_gateway/): FastAPI, Go, GraphQL/REST (support both full and metadata-only queries)
  - [api/](./api/): OpenAPI, protobuf, gRPC
- **Frontend Dashboard**
  - [user_apps/trend_radar/](./user_apps/trend_radar/): Trend Radar (metadata-based)
  - [user_apps/explainable_analytics/](./user_apps/explainable_analytics/): Explainable analytics (deep dive for top-N)
- **MLOps & CI/CD**
  - [orchestration/airflow/](./orchestration/airflow/): Retraining, batch jobs
  - [monitoring/](./monitoring/): Prometheus, Grafana, alerting (monitor pipeline resilience)
- **Documentation**
  - [docs/architecture/](./docs/architecture/): Diagrams, flows
  - [docs/api/](./docs/api/): API reference
  - [docs/development/](./docs/development/): Dev guide

**Deliverables:**
- Public API and dashboard resilient to incomplete data (mass analysis on metadata, deep dive for top-N)
- Interactive dashboard
- Automated retraining and monitoring

---

## Phase 4: Generative AI & Creative Co-Pilot (4-6 months)
**Goal:** Build an AI assistant for content ideation and scenario generation. Generation and recommendations are based mostly on trends and analytics from metadata, deep dive for top-N. RAG context from metadata and top-N video.

### Key Tasks
- **Generative Co-Pilot**
  - [intelligence/generative_copilot/](./intelligence/generative_copilot/): LLM+RAG, scenario generation, optimization loop (metadata-based, deep dive for top-N)
  - [llm_prompts/](./llm_prompts/): Prompt engineering, trend naming, script generation
- **RAG & Retrieval**
  - [intelligence/search_engine/](./intelligence/search_engine/): Vector search, semantic retrieval (metadata and top-N video)
- **User-Facing Apps**
  - [user_apps/script_generator/](./user_apps/script_generator/): Script/idea generator
- **Productization**
  - [api_gateway/](./api_gateway/): Expose generative endpoints

**Deliverables:**
- AI-powered scenario generator and assistant, resilient to missing video/audio (mass analysis on metadata, deep dive for top-N)
- Trend-aware creative assistant
- User-facing tools for content creators

---

## Cross-Cutting Concerns
- **Security & Compliance:** [security/](./security/), [compliance/](./compliance/)
- **Data Governance:** [docs/data_formats/](./docs/data_formats/), [feature_store/](./feature_store/)
- **Experimentation & R&D:** [r_and_d/](./r_and_d/), [research/](./research/)
- **Team & Ownership:** [OWNERS](./OWNERS), [CONTRIBUTING.md](./CONTRIBUTING.md)
- **Resilience to blocking, storage optimization, pipeline quality monitoring**

---

## See Also
- [plan.md](../plan.md) — detailed background, rationale, and technical notes
- [README.md](./README.md) — project overview
- [docs/architecture/](./docs/architecture/) — diagrams, flows, and system design 
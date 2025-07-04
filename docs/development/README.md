# Development Guide

## Getting Started

1. Clone the repository
2. Install prerequisites (see below)
3. Run `make build` and `make run` to start all services

## Prerequisites
- Docker & Docker Compose
- Python 3.10+
- Go 1.20+
- Node.js 18+
- (Optional) Bazel, Airflow, MLflow, etc.

## Useful Commands
- `make build` — build all services
- `make run` — run all services in dev mode
- `make test` — run all tests
- `make lint` — run all linters

## CI/CD
- All PRs are checked by GitHub Actions (see `.github/workflows/`)
- See `CONTRIBUTING.md` for details

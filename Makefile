# Makefile for Prometheus Intelligence Platform
# Use `make help` for available commands

.DEFAULT_GOAL := help
.PHONY: help setup protos lint format test build run deploy-staging deploy-prod clean format lint test pre-commit bazel docker ci

help: ## ✨ Show this help message
	@echo "Available targets:"
	@echo "  format     - Run all formatters (prettier, black, isort)"
	@echo "  lint       - Run all linters (eslint, flake8, pylint, mypy)"
	@echo "  test       - Run all tests (pytest, npm test, go test)"
	@echo "  pre-commit - Run pre-commit on all files"
	@echo "  bazel      - Run Bazel build and test"
	@echo "  docker     - Build Docker images"
	@echo "  ci         - Run full CI pipeline"

setup: ## 🚀 Setup local dev environment
	@echo "--> Setting up environment..."
	./scripts/setup_dev_env.sh

protos: ## 🧬 Generate code from .proto files
	@echo "--> Generating gRPC code..."
	./scripts/gen_protos.sh

lint: ## 🔍 Run linters
	@echo "--> Running linters..."
	# bazel test //... --config=lint

format:
	npx prettier --write .
	black .
	isort .

test: ## 🧪 Run all tests
	@echo "--> Running tests..."
	# bazel test //...

pre-commit:
	pre-commit run --all-files

bazel:
	bazel build //...
	bazel test //...

docker:
	docker build -t prometheus-platform .

ci: format lint test bazel

build: ## 📦 Build all artifacts
	@echo "--> Building project..."
	# bazel build //...

run: ## 🏃 Run core services locally
	@echo "--> Running local services..."
	# docker-compose up

deploy-staging: ## ✈️ Deploy to staging
	@echo "--> Deploying to Staging..."
	# ./scripts/deploy.sh staging

deploy-prod: ## 🚨 Deploy to production
	@echo "--> Deploying to Production..."
	# ./scripts/deploy.sh production

clean: ## 🧹 Clean build artifacts
	@echo "--> Cleaning up..."
	# bazel clean --expunge

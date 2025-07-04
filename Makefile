# Makefile for Prometheus Intelligence Platform
# Use `make help` for available commands

.DEFAULT_GOAL := help
.PHONY: help setup protos lint format test build run deploy-staging deploy-prod clean

help: ## ✨ Show this help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## 🚀 Setup local dev environment
	@echo "--> Setting up environment..."
	./scripts/setup_dev_env.sh

protos: ## 🧬 Generate code from .proto files
	@echo "--> Generating gRPC code..."
	./scripts/gen_protos.sh

lint: ## 🔍 Run linters
	@echo "--> Running linters..."
	# bazel test //... --config=lint

format: ## 🎨 Format all code
	@echo "--> Formatting code..."
	# ./scripts/format.sh

test: ## 🧪 Run all tests
	@echo "--> Running tests..."
	# bazel test //...

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

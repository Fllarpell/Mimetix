# Prometheus Intelligence Platform

## Dev workflow & Code style

- Используйте [EditorConfig](.editorconfig) для единых отступов и концов строк.
- Форматируйте код с помощью [Prettier](.prettierrc.json) (JS/TS/JSON/YAML/MD и др.), [Black](https://black.readthedocs.io/) и [isort](https://pycqa.github.io/isort/) (Python).
- Линтинг: [ESLint](.eslintrc.json) (JS/TS), [flake8](.flake8), [pylint](.pylintrc), [mypy](https://mypy.readthedocs.io/) (Python).
- Все основные правила и исключения — в .editorconfig, .prettierrc.json, .prettierignore, .eslintignore, .gitignore, .bazelignore.

## Pre-commit hooks

- Используйте [pre-commit](https://pre-commit.com/) для автоматической проверки форматирования, линтинга, поиска секретов и ошибок в YAML.
- Установите: `pip install pre-commit`
- Активируйте: `pre-commit install`
- Запустите вручную: `pre-commit run --all-files`

## Linting & Formatting

- JS/TS: `npx eslint .` и `npx prettier --check .`
- Python: `flake8 .`, `pylint .`, `black .`, `isort .`, `mypy .`

## Testing

- JS/TS: `npm test` или `yarn test`
- Python: `pytest`
- Go: `go test ./...`

## CI/CD

- В CI обязательно запускать все форматтеры, линтеры и тесты.
- Используйте remote cache/execution для ускорения сборки (см. .bazelrc).

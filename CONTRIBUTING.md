# Contributing to Prometheus / Участие в проекте Prometheus

## 🇬🇧 English
Thank you for your interest! We welcome all contributions — from typo fixes to new features.

- Please read our [Code of Conduct](./CODE_OF_CONDUCT.md).
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.
- All PRs require review by code owners (see OWNERS file).
- Run `make lint test` before submitting.
- For major changes, open an issue first.

### How to Contribute
1. Fork the repo, create a branch from `main`.
2. Make your changes, add/modify tests.
3. Run all tests and linters.
4. Push and open a Pull Request.
5. PRs are auto-assigned to reviewers based on OWNERS.
6. Address feedback, get approvals, and merge.

## 🇷🇺 Русский
Спасибо за интерес к проекту! Мы рады любому вкладу — от исправления опечаток до новых фичей.

- Ознакомьтесь с [Кодексом поведения](./CODE_OF_CONDUCT.md).
- Используйте [Conventional Commits](https://www.conventionalcommits.org/ru/) для сообщений коммитов.
- Все PR требуют ревью от владельцев кода (см. OWNERS).
- Перед отправкой PR запустите `make lint test`.
- Для крупных изменений сначала создайте Issue.

### Как внести вклад
1. Сделайте форк, создайте ветку от `main`.
2. Внесите изменения, добавьте/обновите тесты.
3. Запустите все тесты и линтеры.
4. Отправьте PR.
5. PR автоматически назначается ревьюерам по OWNERS.
6. Исправьте замечания, получите approve, и PR будет влит.

---

## Commit Message Guidelines / Правила для коммитов
- Format: `<type>(<scope>): <subject>`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Example: `feat(api): add user recommendations endpoint`

## Code Style & Linting
- Python: black, isort, flake8
- Go: gofmt, golangci-lint
- JS/TS: prettier, eslint

## Tests
- Run all tests locally before pushing.
- Use pytest, go test, or npm test as appropriate.

## Communication
- Use GitHub Issues/Discussions for questions and feature requests.
- Be respectful and collaborative — see our Code of Conduct.

.PHONY: help check clean build coverage lint docs pre-commit setup test tox

# Help target to display available commands
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Available targets:"
	@echo "    check         Run pre-commit, docs, tests, and build"
	@echo "    clean         Clean up generated files and caches"
	@echo "    build         Build package distribution"
	@echo "    coverage      Identify code not covered with tests"
	@echo "    lint          Run lint checks on the module"
	@echo "    docs          Build documentation"
	@echo "    pre-commit    Run pre-commit against all files"
	@echo "    setup         Set up the development environment"
	@echo "    test          Run tests (in parallel)"
	@echo "    tox           Run tox (in parallel)"
	@echo "    help          Show this summary of available commands"

# Run all checks
check:
	$(MAKE) pre-commit
	$(MAKE) docs
	$(MAKE) test
	$(MAKE) build

# Clean up generated files and caches
clean:
	find . -name "*.mo" -delete
	find . -name "*.pyc" -delete
	rm -rf .mypy_cache/ .pytest_cache/ .ruff_cache/ dist/ tox/
	rm -rf docs/build/ docs/source/_autosummary/
	rm -f .coverage .coverage.xml

# Build package distribution
build:
	rm -rf *.egg-info/
	python3 -m build

# Run coverage analysis
coverage:
	pytest --cov=brazilcep --cov-config=pyproject.toml --cov-report=term-missing --no-cov-on-fail --cov-report=html

# Run lint checks
lint:
	isort --check brazilcep tests
	black --check brazilcep tests
	ruff check brazilcep tests
	mypy brazilcep

# Build documentation
docs:
	rm -rf docs/build/
	sphinx-autobuild -b html --watch brazilcep/ docs/source/ docs/build/

# Run pre-commit hooks
pre-commit:
	pre-commit run --all-files

# Set up the development environment
setup:
	pip install -e ".[dev]"
	pip install -e ".[coverage]"
	pip install -e ".[docs]"
	pip install -e ".[build]"
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type pre-push
	pre-commit autoupdate
	mypy --install-types

# Run tests
test:
	pytest -v

# Run tox
tox:
	tox --parallel auto

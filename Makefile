.PHONY: help check clean build coverage lint format docs pre-commit setup test test-real test-fast tox install uninstall dev-install update-deps

# Colors for terminal output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

# Project settings
PACKAGE := brazilcep
TESTS := tests
PYTHON := python3
PIP := pip
PYTEST := pytest
SPHINX := sphinx-autobuild

# Help target with colored output
help:
	@echo "$(BLUE)BrazilCEP - Makefile Commands$(NC)"
	@echo ""
	@echo "$(GREEN)Setup & Installation:$(NC)"
	@echo "  $(YELLOW)setup$(NC)           Set up the complete development environment"
	@echo "  $(YELLOW)install$(NC)         Install package in production mode"
	@echo "  $(YELLOW)dev-install$(NC)     Install package in development mode"
	@echo "  $(YELLOW)uninstall$(NC)       Uninstall the package"
	@echo "  $(YELLOW)update-deps$(NC)     Update all dependencies"
	@echo ""
	@echo "$(GREEN)Code Quality:$(NC)"
	@echo "  $(YELLOW)check$(NC)           Run all checks (lint, test, docs, build)"
	@echo "  $(YELLOW)lint$(NC)            Run all linting checks"
	@echo "  $(YELLOW)format$(NC)          Auto-format code with black and isort"
	@echo "  $(YELLOW)pre-commit$(NC)      Run pre-commit hooks on all files"
	@echo ""
	@echo "$(GREEN)Testing:$(NC)"
	@echo "  $(YELLOW)test$(NC)            Run all tests (mocked APIs only)"
	@echo "  $(YELLOW)test-real$(NC)       Run all tests including real API calls"
	@echo "  $(YELLOW)test-fast$(NC)       Run tests without coverage (faster)"
	@echo "  $(YELLOW)coverage$(NC)        Generate detailed coverage report"
	@echo "  $(YELLOW)tox$(NC)             Run tests across multiple Python versions"
	@echo ""
	@echo "$(GREEN)Documentation:$(NC)"
	@echo "  $(YELLOW)docs$(NC)            Build and serve documentation locally"
	@echo "  $(YELLOW)docs-build$(NC)      Build documentation without serving"
	@echo ""
	@echo "$(GREEN)Build & Release:$(NC)"
	@echo "  $(YELLOW)build$(NC)           Build package distribution"
	@echo "  $(YELLOW)clean$(NC)           Clean up generated files and caches"
	@echo "  $(YELLOW)clean-all$(NC)       Deep clean including virtual environments"
	@echo ""
	@echo "$(GREEN)Other:$(NC)"
	@echo "  $(YELLOW)help$(NC)            Show this help message"

# Setup & Installation
setup:
	@echo "$(BLUE)Setting up development environment...$(NC)"
	$(PIP) install -e ".[dev,coverage,docs,build]"
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type pre-push
	pre-commit autoupdate
	mypy --install-types --non-interactive
	@echo "$(GREEN)✓ Development environment ready!$(NC)"

install:
	@echo "$(BLUE)Installing $(PACKAGE)...$(NC)"
	$(PIP) install .
	@echo "$(GREEN)✓ Installation complete!$(NC)"

dev-install:
	@echo "$(BLUE)Installing $(PACKAGE) in development mode...$(NC)"
	$(PIP) install -e ".[dev]"
	@echo "$(GREEN)✓ Development installation complete!$(NC)"

uninstall:
	@echo "$(RED)Uninstalling $(PACKAGE)...$(NC)"
	$(PIP) uninstall -y $(PACKAGE)
	@echo "$(GREEN)✓ Uninstallation complete!$(NC)"

update-deps:
	@echo "$(BLUE)Updating dependencies...$(NC)"
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install --upgrade -e ".[dev,coverage,docs,build]"
	pre-commit autoupdate
	@echo "$(GREEN)✓ Dependencies updated!$(NC)"

# Code Quality
check:
	@echo "$(BLUE)Running all checks...$(NC)"
	@$(MAKE) lint
	@$(MAKE) test
	@$(MAKE) docs-build
	@$(MAKE) build
	@echo "$(GREEN)✓ All checks passed!$(NC)"

lint:
	@echo "$(BLUE)Running linting checks...$(NC)"
	@echo "  → isort..."
	@isort --check $(PACKAGE) $(TESTS) || (echo "$(RED)✗ isort failed$(NC)" && exit 1)
	@echo "  → black..."
	@black --check $(PACKAGE) $(TESTS) || (echo "$(RED)✗ black failed$(NC)" && exit 1)
	@echo "  → ruff..."
	@ruff check $(PACKAGE) $(TESTS) || (echo "$(RED)✗ ruff failed$(NC)" && exit 1)
	@echo "  → mypy..."
	@mypy $(PACKAGE) || (echo "$(RED)✗ mypy failed$(NC)" && exit 1)
	@echo "$(GREEN)✓ All linting checks passed!$(NC)"

format:
	@echo "$(BLUE)Formatting code...$(NC)"
	isort $(PACKAGE) $(TESTS)
	black $(PACKAGE) $(TESTS)
	ruff check --fix $(PACKAGE) $(TESTS) || true
	@echo "$(GREEN)✓ Code formatted!$(NC)"

pre-commit:
	@echo "$(BLUE)Running pre-commit hooks...$(NC)"
	pre-commit run --all-files
	@echo "$(GREEN)✓ Pre-commit checks passed!$(NC)"

# Testing
test:
	@echo "$(BLUE)Running tests (mocked APIs)...$(NC)"
	SKIP_REAL_TEST=True $(PYTEST) -v --tb=short
	@echo "$(GREEN)✓ Tests passed!$(NC)"

test-real:
	@echo "$(YELLOW)Running all tests including real API calls...$(NC)"
	@echo "$(YELLOW)Warning: This may take longer and depends on external APIs$(NC)"
	SKIP_REAL_TEST=False $(PYTEST) -v --tb=short
	@echo "$(GREEN)✓ All tests passed!$(NC)"

test-fast:
	@echo "$(BLUE)Running fast tests (no coverage)...$(NC)"
	SKIP_REAL_TEST=True $(PYTEST) -v -x --tb=short --no-cov
	@echo "$(GREEN)✓ Fast tests passed!$(NC)"

coverage:
	@echo "$(BLUE)Generating coverage report...$(NC)"
	$(PYTEST) \
		--cov=$(PACKAGE) \
		--cov-config=pyproject.toml \
		--cov-report=term-missing \
		--cov-report=html \
		--cov-report=xml \
		--junitxml=junit.xml \
		--no-cov-on-fail
	@echo "$(GREEN)✓ Coverage report generated!$(NC)"
	@echo "$(YELLOW)→ HTML report: htmlcov/index.html$(NC)"

tox:
	@echo "$(BLUE)Running tox across multiple Python versions...$(NC)"
	tox --parallel auto
	@echo "$(GREEN)✓ Tox tests complete!$(NC)"

# Documentation
docs:
	@echo "$(BLUE)Building and serving documentation...$(NC)"
	@echo "$(YELLOW)→ Documentation will be available at http://127.0.0.1:8000$(NC)"
	rm -rf docs/build/
	$(SPHINX) -b html --watch $(PACKAGE)/ docs/source/ docs/build/

docs-build:
	@echo "$(BLUE)Building documentation...$(NC)"
	rm -rf docs/build/
	sphinx-build -b html -W docs/source/ docs/build/
	@echo "$(GREEN)✓ Documentation built!$(NC)"
	@echo "$(YELLOW)→ Open docs/build/index.html$(NC)"

# Build & Release
build:
	@echo "$(BLUE)Building package distribution...$(NC)"
	rm -rf *.egg-info/ dist/
	$(PYTHON) -m build
	@echo "$(GREEN)✓ Package built successfully!$(NC)"
	@echo "$(YELLOW)→ Distribution files in dist/$(NC)"

clean:
	@echo "$(BLUE)Cleaning up generated files...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.mo" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .mypy_cache/ .pytest_cache/ .ruff_cache/ .tox/ htmlcov/
	rm -rf docs/build/ docs/source/_autosummary/
	rm -f .coverage .coverage.* coverage.xml junit.xml
	@echo "$(GREEN)✓ Cleanup complete!$(NC)"

clean-all: clean
	@echo "$(RED)Deep cleaning (including build artifacts)...$(NC)"
	rm -rf dist/ build/
	rm -rf .venv/ venv/ env/
	@echo "$(GREEN)✓ Deep cleanup complete!$(NC)"

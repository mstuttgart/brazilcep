.PHONY : help
help:
	@echo "Usage: make <target>"
	@echo "    check         run pre-commit and tests"
	@echo "    coverage      identify code not covered with tests"
	@echo "    lint          run lint check on module"
	@echo "    docs          run documentation build process"
	@echo "    help          show summary of available commands"
	@echo "    build         build package distribution"
	@echo "    pre-commit    run pre-commit against all files"
	@echo "    setup         setup development environment"
	@echo "    test          run tests (in parallel)"
	@echo "    tox           run tox (in parallel)"

.PHONY : check
check:
	make pre-commit
	make docs
	make test
	make build

.PHONY : clean
clean:
	find . -name *.mo -delete
	find . -name *.pyc -delete
	rm -rf .mypy_cache/*
	rm -rf .pytest_cache/*
	rm -rf .ruff_cache/*
	rm -rf dist/*
	rm -rf docs/build/*
	rm -rf docs/source/_autosummary/*
	rm -rf tox/*
	rm -rf .coverage
	rm -rf .coverage.xml

.PHONY : build
build :
	rm -rf *.egg-info/
	python3 -m build

.PHONY : coverage
coverage:
	pytest --cov=brazilcep --cov-config=pyproject.toml --cov-report term-missing --no-cov-on-fail --cov-report=html

.PHONY : lint
lint:
	isort --check brazilcep tests
	black --check brazilcep tests
	ruff check brazilcep tests
	CUDA_VISIBLE_DEVICES='' pytest -v --color=yes --doctest-modules tests/ brazilcep/

.PHONY : docs
docs:
	rm -rf docs/build/
	sphinx-autobuild -b html --watch brazilcep/ docs/source/ docs/build/

.PHONY : pre-commit
pre-commit:
	pre-commit run --all-files

.PHONY : setup
setup:
	pip install -e ".[dev]"
	pip install -e ".[coverage]"
	pip install -e ".[docs]"
	pip install -e ".[build]"
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type pre-push
	pre-commit autoupdate

.PHONY : test
test:
	pytest

.PHONY : tox
tox:
	tox --parallel auto

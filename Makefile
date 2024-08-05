.PHONY : run-checks
run-checks :
	isort --check .
	black --check .
	ruff check .
	CUDA_VISIBLE_DEVICES='' pytest -v --color=yes --doctest-modules tests/ brazilcep/

.PHONY : build
build :
	rm -rf *.egg-info/
	python -m build

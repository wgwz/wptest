.PHONY: all install-dev test coverage cov docs release clean-pyc

all: test

install-dev:
	pip install -q -e .[dev]

test: clean-pyc install-dev
	pytest

coverage: clean-pyc install-dev
	pip install -q -e .[test]
	coverage run -m pytest
	coverage report
	coverage html

cov: coverage

docs: clean-pyc install-dev
	$(MAKE) -C docs html

release:
	python scripts/make-release.py

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-build: clean-pyc
	rm -rf dist/
	rm -rf build/

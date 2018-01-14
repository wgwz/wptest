.PHONY: all install-dev test coverage cov docs release clean-pyc

all: test

install-dev:
	pip install -q -e .

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

release-sdist:
	python setup.py sdist

release-rpm:
	python setup.py bdist_rpm

build-dev:
	yarn run build --no-minify

build-prod:
	yarn run build

clean: clean-pyc clean-egg clean-build clean-venv

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-egg: 
	find . -name '*.egg-info' -exec rm -rf {} +

clean-build:
	rm -rf dist/
	rm -rf build/

clean-venv:
	find . -name 'venv' -exec rm -rf {} +

clean-edit:
	find . -name '*.sw*' -exec rm -f {} +

.PHONY: all install-dev test coverage cov docs release clean-pyc build-dev build-prod

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

release-sdist:
	python setup.py sdist

release-rpm:
	python setup.py bdist_rpm

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

build-dev:
	yarn run build --no-minify

build-prod:
	yarn run build

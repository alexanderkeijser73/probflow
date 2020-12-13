
.PHONY: init-tensorflow init-pytorch test-tensorflow test-pytorch format docs package push-package clean

init-tensorflow:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -e .[dev,tensorflow]

init-pytorch:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -e .[dev,pytorch]

test-tensorflow:
	. venv/bin/activate; \
	pytest tests/unit/tensorflow

test-pytorch:
	. venv/bin/activate; \
	pytest tests/unit/pytorch

format:
	. venv/bin/activate; \
        isort src/probflow tests; \
	black src/probflow tests; \
	flake8 src/probflow tests

docs:
	. venv/bin/activate; \
	sphinx-build -b html docs docs/_html

package:
	. venv/bin/activate; \
	python setup.py sdist bdist_wheel; \
	twine check dist/*

push-package:
	. venv/bin/activate; \
	twine upload dist/*

clean:
	rm -rf .pytest_cache docs/_html build dist src/probflow.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} \+

install-python:
	@echo "--> Installing Python dependencies"
	pip install -r requirements.txt
	@echo ""

test-python:
	@echo "--> Runing Python tests"
	flake8
	isort -c
	coverage run --source . src/manage.py test src
	coverage report --fail-under=100
	@echo ""

.PHONY: install-python test-python

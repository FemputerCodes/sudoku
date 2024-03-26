# The provided script is a Makefile for managing the project's virtual environment, dependencies, and running the application.

.ONESHELL:

.DEFAULT_GOAL := run

PYTHON	= ./.venv/bin/python3
PIP		= ./.venv/bin/pip3

.PHONY: install run clean

install: requirements.txt
	python3 -m venv .venv
	chmod +x .venv/bin/activate
	. ./.venv/bin/activate
	$(PIP) install -r requirements.txt

venv:
	. ./.venv/bin/activate

run: venv
	$(PYTHON) main.py

clean:
	rm -rf .venv
	find . -type d -name '__pycache__' -exec rm -rf {} \;
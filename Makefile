SHELL := /bin/bash

.PHONY: help clean install runserver test migrate check black flake8 mypy lint


install:
    pip install -r requirements.txt

runserver:
    python manage.py runserver

migrate:
    python manage.py makemigrations && python manage.py migrate

check: black flake8 mypy

black:
    black .

flake8:
    flake8 .

mypy:
    mypy .

lint: black flake8 mypy

clean:
    find . -name '*.pyc' -delete
    find . -name '__pycache__' -type d -exec rm -rf {} +

docker_stop:
    docker stop $(docker ps -q)

SHELL := /bin/bash

.PHONY: help clean install runserver test migrate check black flake8 mypy lint

help:
 @echo 'Usage:'
 @echo '    make install      Install dependencies'
 @echo '    make runserver    Run development server'
 @echo '    make migrate      Apply database migrations'
 @echo '    make check        Check code quality'
 @echo '    make black        Format code with Black'
 @echo '    make flake8       Lint code with Flake8'
 @echo '    make mypy         Type-check code with Mypy'
 @echo '    make lint         Run all linters'
 @echo '    make clean        Clean up project'

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

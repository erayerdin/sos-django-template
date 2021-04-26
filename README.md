# SOS Django Template

![License](https://img.shields.io/badge/license-WTFPL-black.svg?style=flat-square)
![Version](https://shields.io/github/v/release/erayerdin/sos-django-template?style=flat-square)
![Python Version](https://img.shields.io/badge/-3.7%2B-blue.svg?style=flat-square&logo=python&logoColor=white)
![Django Version](https://img.shields.io/badge/-2.2%2B-0C4B33.svg?style=flat-square&logo=django&logoColor=white)

SOS Django Tempalate is a Django starter template that has opinionated and good solutions while starting your new Django project.

Django is a batteries-included backend framework. While it comes with a good starting template, this boilerplate is not usually enough for developing your projects further. So, you will often find yourself installing 3rd party packages, configuring them and structuring your project according to these 3rd party solutions, which is a waste of time. Instead, SOS Django Template starts you from opinionated but sensible defaults.

You can [refer to the documentation](https://github.com/erayerdin/sos-django-template/wiki) in order to start using it.

## Environment

SOS Django Template requires Python 3.7+, Django 2.2+ and [Poetry](https://python-poetry.org/) to be installed on your system.

This template separates production and development settings, which are under different `project.settings.development` and `project.settings production` modules.

It comes with [many dependencies](https://github.com/erayerdin/sos-django-template/wiki/Power-Cable-Included:-What-comes-with-SOS-Django-Template%3F) ready to use, such as black, flake8, isort, pytest, Django Rest Framework, Celery etc.

## How to Use

You can see how to use it [here](https://github.com/erayerdin/sos-django-template/wiki/Requirements-and-Installation). A quick start would be:

```bash
# start a project named PROJECT_NAME
django-admin startproject PROJECT_NAME --template https://github.com/erayerdin/sos-django-template/archive/master.zip

# go to project root
cd PROJECT_NAME

# install system dependencies
bash ubuntu20.requirements.bash

# change project info
xdg-open pyproject.toml
xdg-open LICENSE.txt

# initialize poetry
poetry shell

# install deps
poetry install
# --no-dev flag to install only prod deps

# add pre-commit hooks, optional, recommended
pre-commit install

# change .env
mv .env.example .env  # rename
xdg-open .env  # edit
```

## Documentation

This repository has a [Wiki section](https://github.com/erayerdin/sos-django-template/wiki) so you can use it to get further information as to how to install and use SOS Django Template *and* tips and tricks.

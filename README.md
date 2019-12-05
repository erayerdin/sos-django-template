# SOS Django Template

![Travis (.com)](https://img.shields.io/travis/com/erayerdin/sos-django-template/master.svg)
![License](https://img.shields.io/badge/license-WTFPL-black.svg)
![Version](https://img.shields.io/badge/version-0.3.1-green.svg)
![Python Version](https://img.shields.io/badge/-python%203.6%2B-blue.svg)
![Django Version](https://img.shields.io/badge/-django%202.2%2B-0C4B33.svg)

SOS (Separation of Settings) Django Template is a Django
template, hence the name, separates the settings into
development and production environment. However, it does
not only do separate settings, it creates an
_opinionated_ starter environment for Django by
including a couple more packages to install and more features.

 > #### Warning
 >
 > If you would like to contribute, see "Notes" section below.

## How to Use

`django-admin startproject` command accepts `--template`
flag. This template argument accepts a URL that points
to a zip file.

The `master` branch of this repository is considered to
be stable. So, adding `archive/master.zip` to the URL of
this repo should be enough, see below:

```
https://github.com/erayerdin/sos-django-template/archive/master.zip
```

So, now you can use this URL with `django-admin` to
start your project:

```bash
django-admin startproject yourProjectName --template https://github.com/erayerdin/sos-django-template/archive/master.zip
```

The rest is pretty standard stuff, you would like
to (i) create a virtual environment, (ii) activate it
and (iii) install dependencies as so:

```bash
virtualenv .venv # (i)
source .venv/bin/activate # (ii)
pip install -r requirements.txt # (iii)
pip install -r dev.requirements.txt # (iii)
```

You also might want to install pre-commit in order to
check the style and sort the imports before committing.

```bash
pre-commit install
```

The first time might take a couple of minutes.

## Environment

This template requires:

- Minimum Python 3.6
- Minimum Django 2.2

This template includes these with production in mind:

- [Celery](https://docs.celeryproject.org/en/latest/) for scheduled and asyncronous tasks
- [Django Rest Framework](http://django-rest-framework.org/) for REST applications and building AJAX-based applications

Also, these with development in mind:

- [Django Debug Tooolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#getting-the-code), which is a handy tool that provides information about template generation, query building etc.
- [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers), which allows CORS requests in only development environment and overcomes the pain of CORS errors during development
- [Pytest Django](https://pytest-django.readthedocs.io/en/latest/), which integrates amazing [pytest](https://docs.pytest.org/en/latest/) testing framework with Django
- [Pytest PUDB](https://github.com/wronglink/pytest-pudb) is a tool that you can
use to debug Django/Python on terminal with [pudb](https://github.com/inducer/pudb).
- [Black](https://black.readthedocs.io/en/stable/), which is a on-the-fly Python code formatter and linter
- [Isort](https://isort.readthedocs.io/en/latest/), which sorts imports on-the-fly
- [ipython](https://ipython.org/), which spawns when you `python3 manage.py shell`.

## Architecture and Design Choices

SOS Django Template aims to provide a solid foundation
with well-known packages for the solutions
_targeting backend_. The file structure is slightly
modified for better development.

### Settings

SOS Django Template, hence its name, separates Django
settings to development and production environments.

All settings are located in `project.settings` as
a package and this package contains three separate
modules:

- **`project.settings.defaults` module:** This module
  contains _default_ settings that are generated with
  `django-admin startproject`.
- **`project.settings.base` module:** This module
  contains the settings in both _production_ and
  _development_ environment.
- **`project.settings.development` module**
- **`project.settings.production` module**

When the Django application is called within the
terminal, it must point to either `development` or
`production` module. By default, `manage.py` uses
`development` module and `project/wsgi.py` uses
`production` module.

The overall import schema for settings are as below:

```
defaults
└── base
    ├── development
    └── production
```

### Celery

The template includes Celery and `project` is configured
to be ready to use Celery, but Celery configurations
have not been defined. If you want to use Celery, you
need to configure your message broker and results
backend. [This article][django_celery_article] shows
an example.

[django_celery_article]: https://realpython.com/asynchronous-tasks-with-django-and-celery/

### Fixtures

You can define your pytest fixtures inside
`project.fixtures` package. If you want to define your
fixture in a separate module inside `fixtures`, then
you need to import that in `__init__.py`.

```python
# project.fixtures

from .auth import user_factory, token_factory
# these are examples
```

### EditorConfig

This project also provides a `.editorconfig` file to instruct your editor or IDE
and keep your files clean. Check [the file](.editorconfig) to see what files are
affected by this.

## Notes

- `black` and `isort` is not bound by a git hook by default. You should
  integrate them with `pre-commit install` at first install.
 - If you intend to contribute to the project, please **target
 `development` environment**. `development` branch is supposed
 to have the latest stuff.

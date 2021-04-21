# SOS Django Template

![License](https://img.shields.io/badge/license-WTFPL-black.svg?style=flat-square)
![Version](https://shields.io/github/v/release/erayerdin/sos-django-template?style=flat-square)
![Python Version](https://img.shields.io/badge/-3.7%2B-blue.svg?style=flat-square&logo=python&logoColor=white)
![Django Version](https://img.shields.io/badge/-2.2%2B-0C4B33.svg?style=flat-square&logo=django&logoColor=white)

SOS (Separation of Settings) Django Template is a Django template, hence the name, separates the settings into development and production environment. However, it does not only do separate settings, it creates an _opinionated_ starter environment for Django by including a couple more packages to install and more features.

 > #### Warning
 >
 > If you would like to contribute, see "Notes" section below.

## Environment

This template requires:

- Minimum Python 3.7
- Minimum Django 2.2
- Poetry

The production and development Python requirements are defined in `pyproject.toml` file. The system requirements are defined in `<SYSTEM_NAME>.requirements.txt` files (currently, we only have requirements for Ubuntu).

This template includes these with production environment in mind:

- [Celery](https://docs.celeryproject.org/en/latest/) for scheduled and asyncronous tasks
- [Django Rest Framework](http://django-rest-framework.org/) for REST applications and building AJAX-based applications

Also, these with development in mind:

- [Poetry](https://python-poetry.org/), which is a great dependency management and isolation solution rather than manually specifying dependencies on separate files.
- [Django Debug Tooolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#getting-the-code), which is a handy tool that provides information about template generation, query building etc.
- [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers), which allows CORS requests in only development environment and overcomes the pain of CORS errors during development
- [Pytest Django](https://pytest-django.readthedocs.io/en/latest/), which integrates amazing [pytest](https://docs.pytest.org/en/latest/) testing framework with Django
- [Pytest PUDB](https://github.com/wronglink/pytest-pudb) is a tool that you can
use to debug Django/Python on terminal with [pudb](https://github.com/inducer/pudb).
 - [Pytest Factoryboy](http://pytest-factoryboy.rtfd.io/) is a tool to create instances with ease and use it as pytest fixtures.
- [environs](https://github.com/sloria/environs) to load your `.env` variables
- [Black](https://black.readthedocs.io/en/stable/), which is a on-the-fly Python code formatter and linter
- [Isort](https://isort.readthedocs.io/en/latest/), which sorts imports on-the-fly
- [flake8](https://gitlab.com/pycqa/flake8) to lint your code
- [ipython](https://ipython.org/), which spawns when you `python3 manage.py shell`.

## How to Use

`django-admin startproject` command accepts `--template` flag. This template argument accepts a URL that points to a zip file.

The `master` branch of this repository is considered to be stable. So, adding `archive/master.zip` to the URL of this repo should be enough, see below:

```
https://github.com/erayerdin/sos-django-template/archive/master.zip
```

So, now you can use this URL with `django-admin` to start your project:

```bash
django-admin startproject yourProjectName --template https://github.com/erayerdin/sos-django-template/archive/master.zip
```

You can also view [releases](https://github.com/erayerdin/sos-django-template/releases) and select specific one to install. To install a specific version, you can:

```bash
django-admin startproject yourProjectName --template https://github.com/erayerdin/sos-django-template/archive/refs/tags/<VERSION_HERE>.zip
```

After `cd`'ing into project directory, the first thing you need to do is to install platform-specific dependencies on your system. Currently, only Ubuntu dependencies are provided. PRs are welcome if you'd like to specify dependencies for other platforms. To install platform-specific dependencies:

```bash
sudo apt install $(cat ubuntu.requirements.txt)
```

After this, you can launch poetry shell and install dependencies:

```bash
poetry shell
poetry install
```

After doing these steps, you better check `.env.example`  file on the project root. You have to copy/move/rename it  as `.env` and **set `DJANGO_SECRET_KEY` environment  variable before running Django** or *Django will not run*.

You also might want to install pre-commit in order to check the style and sort the imports before committing.

```bash
pre-commit install
```

The first time for pre-commit to install might take a  couple of minutes.

## Architecture and Design Choices

SOS Django Template aims to provide a solid foundation with well-known packages for the solutions _targeting backend_. The file structure is slightly modified for better development.

### Settings

SOS Django Template, hence its name, separates Django settings to development and production environments.

All settings are located in `project.settings` as a package and this package contains three separate modules:

- **`project.settings.defaults` module:** This module
  contains _default_ settings that are generated with
  `django-admin startproject`.
- **`project.settings.base` module:** This module
  contains the settings in both _production_ and
  _development_ environment.
- **`project.settings.development` module**
- **`project.settings.production` module**

When the Django application is called within the terminal, it must point to either `development` or `production` module. By default, `manage.py` uses `development` module and `project/wsgi.py` uses `production` module.

The overall import schema for settings are as below:

```
defaults
└── base
    ├── development
    └── production
```

### Core App

`core` app is a built-in custom app comes with this template. It includes various features such as:

 - `TimestampModel` and `ExtendedTimestampModel` models in order to automatically define `created_at` and `last_update` fields in your model
 - A custom `CoreUser` model

#### Timestamp Models

Laravel automatically injects object creation and update datetimes into the models. You have to specifically specify them in Django. However, this template has two different timestamp models called `TimestampModel` and `ExtendedTimestampModel`. You can use these models to inject these fields into your models automatically.

`TimestampModel` only has `created_at` field whereas `ExtendedTimestampModel` has both `created_at` and `last_update` fields. In order to use them:

```python
from core.models import TimestampModel, ExtendedTimestampModel

# ...

class Foo(TimestampModel):
  # ...

class Bar(ExtendedTimestampModel):
  # ...

foo = Foo.objects.create()
foo.created_at  # returns when it is created

bar = Bar.objects.create()
bar.created_at
bar.last_update  # returns when it is last updated
```

#### Core User

A custom user model *must be defined as early as possible*, that's why this template comes with built-in `CoreUser` model, which is the default user model. You can edit and add extra fields to `CoreUser` model on `core/models.py`.

### PostgreSQL

SOS Django Template already assumes that you will use PostgreSQL. It installs and is preconfigured to work with PostgreSQL. Check your `.env.example` file in the project root to further configure your setup.

### DotEnv

[Due to twelve-factor app conventions](https://12factor.net/config), separating your configuration from application is considered to be a better practice. SOS Django Template comes batteries included to use `.env` files in your codebase and already has a `.env.example` file. You have to copy this file to your project root as `.env` for your project to run.

After copying, you better review your config file to make some changes such as secret key and database settings.

Under the hood, SOS Django Template uses [environs](https://github.com/sloria/environs#usage-with-django) to read your configurations. You probably would like to check their documentations out in order to create your extra configurations.

### Celery

The template includes Celery and `project` is configured to be ready to use Celery, but Celery configurations have not been defined. If you want to use Celery, you need to configure your message broker and results backend. [This article][django_celery_article] shows an example.

[django_celery_article]: https://realpython.com/asynchronous-tasks-with-django-and-celery/

### Fixtures

You can define your pytest fixtures inside `project.fixtures` package.

```python
import pytest

@pytest.fixture
def token():
    # some operations to generate token
```

You can also separate your fixtures inside `project.fixtures` package, but you also need to import it in `__init__.py` in `project.fixtures` package. Assuming you have `project.fixtures.auth` module and the `token` fixture above put into it:

```python
# file: project/fixtures/auth.py
import pytest

@pytest.fixture
def token():
    # some operations to generate token

# file: project/fixtures/__init__.py
from .auth import *  # noqa

# noqa comment will make your linter/formatter to not complain about the import
```

### Pytest Factoryboy

[Pytest Factoryboy](https://github.com/pytest-dev/pytest-factoryboy) is a great way to create factories in your project, similar to [Laravel's factories](https://laravel.com/docs/master/database-testing). In order to create a factory, you need to have `factories.py` module in one of your apps. The built-in `core` module in SOS Django Template already has `CoreUserFactory` in `factories.py` module, [check it out](core/factories.py).

Also make sure to add your `factories` module to `conftest.py`'s `pytest_plugins` array at the root of your project, [core module already has been added to it](conftest.py). In order to create a `CoreUser` instance, you can either (i) get a quick instance of it by simply using `core_user` fixture or (ii) use `core_user_factory` fixture to create custom or more than one author in a test. See the example below:

```python
def test_foo(core_user):
    # test something with CoreUser instance

def test_bar(core_user_factory):
    # create a custom CoreUser
    user = core_user_factory(username="johndoe")

    # or create 10 users
    for _ in range(10):
        core_user_factory()

    # and do some tests
```

Built-in `core_user` and `core_user_factory` fixtures are safe to use in multiple creations. `username` and `email` fields are automatically generated as `user{ORDER}` and `user{ORDER}@example.com`. Since factories are meant to be used in tests, the `password` field will always result in `111111`.

### EditorConfig

This project also provides a `.editorconfig` file to instruct your editor or IDE and keep your files clean. Check [the file](.editorconfig) to see what files are affected by this.

## Notes

 - `black` and `isort` is not bound by a git hook by default. You should integrate them with `pre-commit install` at first install.
 - If you intend to contribute to the project, please **target `development` environment**. `development` branch is supposed to have the latest stuff.
 - By default, this template ignores `poetry.lock` file. [You should change this behavior](https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control) by removing `poetry.lock` line in [.gitignore file](.gitignore).

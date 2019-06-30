# SOS Django Template

![Travis (.com)](https://img.shields.io/travis/com/erayerdin/sos-django-template/master.svg)
![Python Version](https://img.shields.io/badge/-python%203.6%2B-blue.svg)
![Django Version](https://img.shields.io/badge/-django%202.2%2B-0C4B33.svg)

SOS (Separation of Settings) Django Template is a Django
template, hence the name, separates the settings into
development and production environment. However, it does
not only do separate settings, it creates an
_opinionated_ starter environment for Django by
including a couple more packages to install.

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

## Environment

This template requires:

- Minimum Python 3.6
- Minimum Django 2.2

This template includes:

- [Django Rest Framework](http://django-rest-framework.org/) for REST applications and building AJAX-based applications
- [Django Debug Tooolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#getting-the-code), which is a handy tool that provides information about template generation, query building etc.
- [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers), which allows CORS requests in only development environment and overcomes the pain of CORS errors during development
- [Pytest Django](https://pytest-django.readthedocs.io/en/latest/), which integrates amazing [pytest](https://docs.pytest.org/en/latest/) testing framework with Django
- [Black](https://black.readthedocs.io/en/stable/), which is a on-the-fly Python code formatter and linter
- [Isort](https://isort.readthedocs.io/en/latest/), which sorts imports on-the-fly

## Notes

- `black` and `isort` is not bound by a git hook, so
  you should either integrate these with your editor or
  your git hooks in your local repository.

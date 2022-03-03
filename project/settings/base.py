"""
Contains settings for both development and production environment.
"""

from environs import Env

from .defaults import *

env = Env()
env.read_env()

# Django
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env.bool("DJANGO_DEBUG", default=True)
WSGI_APPLICATION = "project.wsgi.application"
LANGUAGE_CODE = env.str("DJANGO_LANGUAGE_CODE", "en-us")
TIME_ZONE = env.str("DJANGO_TIME_ZONE", "UTC")
USE_I18N = env.bool("DJANGO_USE_I18N", True)
USE_L10N = env.bool("DJANGO_USE_L10N", True)
USE_TZ = env.bool("DJANGO_USE_TZ", True)
DATABASES = {
    "default": {
        "ENGINE": env.str("DJANGO_DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": env.str("DJANGO_DB_NAME", default=BASE_DIR / "db.sqlite3"),
        "USER": env.str("DJANGO_DB_USER", default="postgres"),
        "PASSWORD": env.str("DJANGO_DB_PASSWORD", default="nopassword"),
        "HOST": env.str("DJANGO_DB_HOST", default="127.0.0.1"),
        "PORT": str(env.int("DJANGO_DB_PORT", default=5432)),
    }
}
STATIC_URL = env.str("DJANGO_STATIC_URL", "/static/")
ROOT_URLCONF = "project.urls"

# Django Extensions
INSTALLED_APPS.append("django_extensions")

# Rest Framework
INSTALLED_APPS.append("rest_framework")

# Core App
INSTALLED_APPS.append("core")
AUTH_USER_MODEL = "core.CoreUser"

# Celery
# TODO celery config
# You can add your own configuration for Celery here.
# You can use below as reference:
# https://realpython.com/asynchronous-tasks-with-django-and-celery/

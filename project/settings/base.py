"""
Contains settings for both development and production environment.
"""

from .defaults import *

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

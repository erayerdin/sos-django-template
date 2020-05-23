"""
Contains settings for both development and production environment.
"""

import warnings
from .defaults import *

# Rest Framework
INSTALLED_APPS.append("rest_framework")

# Celery
# TODO celery config
# You can add your own configuration for Celery here.
# You can use below as reference:
# https://realpython.com/asynchronous-tasks-with-django-and-celery/

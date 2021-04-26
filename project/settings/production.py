"""
Contains settings for only production environment.
"""

import warnings

from .base import *  # noqa

DEBUG = False

STATIC_ROOT = env.str("DJANGO_STATIC_ROOT")

warnings.warn("Do not forget to set ALLOWED_HOSTS variable.", RuntimeWarning)

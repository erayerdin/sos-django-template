"""
Contains settings for only production environment.
"""

import warnings

from .base import *  # noqa

DEBUG = False

warnings.warn("Do not forget to set ALLOWED_HOSTS variable.", RuntimeWarning)

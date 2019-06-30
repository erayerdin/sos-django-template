"""
Contains settings for both development and production environment.
"""

import os, warnings
from textwrap import dedent
from .defaults import *

# Secret Key
__secret_key_env = os.environ.get("DJANGO_SECRET_KEY", None)

if __secret_key_env:
    SECRET_KEY = __secret_key_env
else:
    __message = """
    DJANGO_SECRET_KEY environment variable is not set.
    Using secret key provided by Django on project
    generation for debugging/development purposes.
    Do not forget to set DJANGO_SECRET_KEY in
    production environment.
    """
    __message = dedent(__message)
    warnings.warn(__message, RuntimeWarning)


# Rest Framework
INSTALLED_APPS.append("rest_framework")
"""
Contains settings for only development environment.

Note: DEBUG is already set to True in defaults.
"""
import tempfile

from .base import *

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ["127.0.0.1"]

# Static Files
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", str(Path(tempfile.gettempdir()) / "django"))

# Debug Toolbar
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# Cors Headers
INSTALLED_APPS.append("corsheaders")
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")
CORS_ORIGIN_ALLOW_ALL = True

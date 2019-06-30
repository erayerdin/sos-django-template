import os
import warnings

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.development")

app = Celery("project")
warnings.warn(
    "You might want to change the name of your Celery application. Defaults to: project"
)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

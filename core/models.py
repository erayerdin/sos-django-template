from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ExtendedTimestampModel(TimestampModel):
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

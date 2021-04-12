from django.contrib.auth.models import AbstractUser
from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ExtendedTimestampModel(TimestampModel):
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# see: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser
# update this model for custom fields on User model
class CoreUser(AbstractUser):
    pass

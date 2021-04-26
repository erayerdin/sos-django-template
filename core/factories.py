import factory
from django.contrib.auth.hashers import make_password
from pytest_factoryboy import register

from core import models


@register
class UserFactory(factory.django.DjangoModelFactory):
    password = factory.LazyFunction(lambda: make_password("111111"))
    is_superuser = False
    is_staff = False
    is_active = True

    class Meta:
        model = models.CoreUser

    @factory.lazy_attribute
    def username(self):
        count = models.CoreUser.objects.count() + 1
        return f"user{count}"

    @factory.lazy_attribute
    def email(self):
        count = models.CoreUser.objects.count() + 1
        return f"user{count}@example.com"

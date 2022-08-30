import pytest
import factory
from users.models import Users


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Users
        django_get_or_create = ('email',)

    email = 'steven.ghzv@gmail.com'
    full_name = 'Steven Qzvi'
    password = '123456'

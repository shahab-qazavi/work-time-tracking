import factory
from users.tests.factories import UserFactory
from tasks.models import Tasks


class CreateTaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tasks

    assignment = factory.SubFactory(UserFactory)
    title = 'some title'
    description = 'some description'


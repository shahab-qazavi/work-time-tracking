from parameterized import parameterized
from django.test import RequestFactory, TestCase
from django.urls import reverse
from users.tests.factories import UserFactory
from tasks import views


class TestCreateTask(TestCase):

    def setUp(self) -> None:
        self.url = reverse('create')
        self.view = views.TasksCreate
        user = UserFactory.create()
        self.user = user.save()

    @parameterized.expand([('title for test', 'description for test', 200)])
    def test_create_task(self, title, description, status):
        data = {'assignment': self.user, 'title': title, 'description': description}
        status = status
        request = RequestFactory().post(self.url, data=data)
        response = self.view.as_view()(request)
        assert response.status_code == status, f'failed user creation test: {data}' + 'must be' + str(status) + \
                                               'but its' + str(response.status_code)

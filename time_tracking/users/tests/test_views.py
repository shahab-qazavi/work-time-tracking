import pytest
from parameterized import parameterized
from django.test import RequestFactory, TestCase
from django.urls import reverse
from .factories import UserFactory
from users import views


class TestUserCreate(TestCase):

    def setUp(self) -> None:
        self.url = reverse('register')
        self.view = views.RegisterView

    @parameterized.expand([('steven.ghzv@gmail.com', '123456', 200),
                           ('steven.ghzv@gmail.com', '123456', 400), ])
    def test_create_user(self, email, password, status):
        data = {'email': email, 'password': password}
        status = status
        request = RequestFactory().post(self.url, data=data)
        response = self.view.as_view()(request)
        assert response.status_code == status, f'failed user creation test: {data}' + 'must be' + str(status) +\
                                               'but its' + str(response.status_code)


class TestUserLogin(TestCase):

    def setUp(self) -> None:
        self.url = reverse('login')
        self.view = views.LoginView
        user = UserFactory
        user.create()

    @parameterized.expand([('steven.ghzv@gmail.com', '123456', 200),
                           ('steven.ghzv@gmail.com', '123456steven', 400), ])
    def test_create_user(self, email, password, status):
        data = {'email': email, 'password': password}
        status = status
        request = RequestFactory().post(self.url, data=data)
        response = self.view.as_view()(request)
        assert response.status_code == status, f'failed user creation test: {data}' + 'must be' + str(status) + \
                                               'but its' + str(response.status_code)


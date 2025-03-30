import datetime
from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse
from users.models import Profile
from users.forms import UserRegisterForm, UserLoginForm
from django.utils import timezone


# class TestRegistration(TestCase):

#     def setUp(self):
#         self.data = {'username': 'ol',
#                      'birth_date': '05/02/1999',
#                      'email': 'Jack@mail.ru',
#                      'password1': 'pereck99',
#                      'password2': 'pereck99'}
#         self.path = reverse('users:registration')

#     def test_registration_post(self):
#         self.assertFalse(Profile.objects.filter(username=self.data['username']).exists())
#         response = self.client.post(self.path, self.data)
#         self.assertEqual(response.status_code, HTTPStatus.FOUND)
#         self.assertRedirects(response, reverse('products:index'))
#         self.assertTrue(Profile.objects.filter(username=self.data['username']).exists())

#     def test_registration_form(self):
#         form = UserRegisterForm()
#         # username - без лэйбла
#         self.assertFalse(form.fields['username'].label == None)
#         # birthday - дата в прошлом
#         date = datetime.date.today() - datetime.timedelta(days=1)
#         form_data = {'birth_date': date}
#         form = UserRegisterForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         # Дата не в будущем
#         date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
#         form_data = {'birth_date': date}
#         form = UserRegisterForm(data=form_data)
#         self.assertFalse(form.is_valid())

class TestRegistration(TestCase):
    def setUp(self):
        self.data = {'username': 'TestUser',
                     'birth_date': '1999-02-05',
                     'email': 'testuser@mail.ru',
                     'password1': 'pereck99',
                     'password2': 'pereck99'}
        self.username = 'TestUser',
        self.birth_date = '1999-02-05',
        self.email = 'testuser@mail.ru',
        self.password1 = 'pereck99',
        self.password2 = 'pereck99'

    def test_registration(self):
        self.assertFalse(Profile.objects.filter(username=self.username).exists())
        user = Profile.objects.create_user(username=self.data['username'],
                                           birth_date=self.data['birth_date'],
                                           email=self.data['email'],
                                           password=self.data['password1'],)
        user.save()
        self.assertTrue(Profile.objects.filter(username=self.data['username']).exists())
        self.client.login(username=self.data['username'],
                          password=self.data['password1'])
        self.client.logout()


class TestLogin(TestCase):

    def setUp(self):
        self.data = {'username': 'TestUser',
                     'password': 'pereck99'}
        self.path = reverse('users:login')
        self.user = Profile.objects.create_user(username=self.data['username'],
                                                password=self.data['password'],)

    def test_login(self):
        self.assertTrue(Profile.objects.get(username=self.data['username']))
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('products:index'))
        self.assertTrue(Profile.objects.filter(username=self.data['username']).exists())

    def test_login_not_found(self):
        self.assertFalse(Profile.objects.filter(username='new_user').exists())

from django.contrib.auth.models import User
from django.test import TestCase


class Login(TestCase): 
    def setUp(self)
        self.credentials ={
            'username': 'prueba',
            'password1': 'prueba12345'}
        User.objects.create_user(**self.credentials)

    def logeo(self)
        response = self.client.post('/login', self.credentials, follow = True)

        self.assertTrue(response.context['user'].is_active)       
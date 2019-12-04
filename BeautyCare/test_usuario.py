from django.contrib.auth.models import User
from django.test import TestCase


class UsuarioTest(TestCase):
    def setUp(self):
        self.usuario1 = {
            'username': 'user1',
            'email': 'user1@gmail.com',
            'password': 'user12345'}
        User.objects.create_user(**self.user1)

        self.usuario2 = {
            'username': 'user2',
            'email': 'user2@gmail.com',
            'password': 'user21234'}
        User.objects.create_user(**self.user2)

    def test_usuario_username(self):
        usuario = User.objects.get(username="user1")
        self.assertEqual(usuario.username, "user1")

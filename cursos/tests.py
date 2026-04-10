from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Curso

class CursoTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.curso = Curso.objects.create(
            nombre='Química Orgánica',
            descripcion='Curso de nivel intermedio'
        )

    def test_acceso_cursos_con_token(self):
        response = self.client.get('/api/cursos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_acceso_cursos_sin_token(self):
        self.client.credentials()
        response = self.client.get('/api/cursos/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_crear_curso(self):
        response = self.client.post('/api/cursos/', {
            'nombre': 'Química Inorgánica',
            'descripcion': 'Curso básico'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_cursos(self):
        response = self.client.get('/api/cursos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from cursos.models import Curso
from .models import Leccion

class LeccionTests(TestCase):

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
        self.leccion = Leccion.objects.create(
            curso=self.curso,
            titulo='Introducción',
            contenido='Contenido de prueba',
            orden=1
        )

    def test_listar_lecciones(self):
        response = self.client.get('/api/lecciones/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_acceso_sin_token(self):
        self.client.credentials()
        response = self.client.get('/api/lecciones/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
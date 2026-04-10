from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from cursos.models import Curso
from lecciones.models import Leccion
from .models import Evaluacion

class EvaluacionTests(TestCase):

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
            descripcion='Curso intermedio'
        )
        self.leccion = Leccion.objects.create(
            curso=self.curso,
            titulo='Lección 1',
            contenido='Contenido',
            orden=1
        )
        self.evaluacion = Evaluacion.objects.create(
            leccion=self.leccion,
            pregunta='¿Cuál es el símbolo del oxígeno?',
            opcion_a='O',
            opcion_b='Ox',
            opcion_c='Og',
            respuesta_correcta='A'
        )

    def test_listar_evaluaciones(self):
        response = self.client.get('/api/evaluaciones/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_respuesta_correcta(self):
        response = self.client.post('/api/responder/', {
            'evaluacion': self.evaluacion.id,
            'respuesta': 'A'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['correcta'])

    def test_respuesta_incorrecta(self):
        response = self.client.post('/api/responder/', {
            'evaluacion': self.evaluacion.id,
            'respuesta': 'B'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data['correcta'])
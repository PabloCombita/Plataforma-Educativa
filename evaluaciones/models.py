from django.db import models
from django.conf import settings
from lecciones.models import Leccion

class Evaluacion(models.Model):
    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        related_name='evaluaciones'
    )
    pregunta = models.TextField()
    opcion_a = models.CharField(max_length=200)
    opcion_b = models.CharField(max_length=200)
    opcion_c = models.CharField(max_length=200)
    respuesta_correcta = models.CharField(
        max_length=1,
        choices=[('A','A'),('B','B'),('C','C')]
    )

    def __str__(self):
        return self.pregunta

class IntentoEvaluacion(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    evaluacion = models.ForeignKey(
        Evaluacion,
        on_delete=models.CASCADE
    )
    respuesta = models.CharField(max_length=1)
    es_correcta = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.evaluacion}"

class ProgresoCurso(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    curso = models.ForeignKey(
        'cursos.Curso',
        on_delete=models.CASCADE
    )
    porcentaje = models.FloatField(default=0)

    def __str__(self):
        return f"{self.usuario} - {self.curso} ({self.porcentaje}%)"

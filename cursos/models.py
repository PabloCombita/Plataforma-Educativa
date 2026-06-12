from django.conf import settings
from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["id"]

    def __str__(self):
        return self.nombre


class InscripcionCurso(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Inscripción a curso"
        verbose_name_plural = "Inscripciones a cursos"
        unique_together = ("usuario", "curso")
        ordering = ["id"]

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.nombre}"
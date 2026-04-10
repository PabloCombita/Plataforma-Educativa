from django.db import models
from cursos.models import Curso

class Leccion(models.Model):
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='lecciones'
    )
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    orden = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
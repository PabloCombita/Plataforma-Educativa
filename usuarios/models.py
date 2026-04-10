from django.db import models
from django.conf import settings

class PerfilUsuario(models.Model):
    ROL_CHOICES = [
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
        ('admin', 'Administrador'),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    rol = models.CharField(
        max_length=20,
        choices=ROL_CHOICES,
        default='estudiante'
    )
    foto = models.ImageField(
        upload_to='fotos_perfil/',
        null=True,
        blank=True
    )
    bio = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Curso, InscripcionCurso


User = get_user_model()


class CursoSerializer(serializers.ModelSerializer):
    total_inscritos = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = "__all__"

    def get_total_inscritos(self, obj):
        return obj.inscripciones.filter(activa=True).count()


class InscripcionCursoSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source="usuario.username", read_only=True)
    usuario_email = serializers.CharField(source="usuario.email", read_only=True)
    curso_nombre = serializers.CharField(source="curso.nombre", read_only=True)

    class Meta:
        model = InscripcionCurso
        fields = [
            "id",
            "usuario",
            "usuario_username",
            "usuario_email",
            "curso",
            "curso_nombre",
            "fecha_inscripcion",
            "activa",
        ]


class UsuarioParaInscripcionSerializer(serializers.ModelSerializer):
    rol = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "is_superuser", "rol"]

    def get_rol(self, obj):
        if obj.is_staff or obj.is_superuser:
            return "admin"
        return "estudiante"
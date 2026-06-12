from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from plataforma_quimica.permissions import IsAdminRole
from .models import Curso, InscripcionCurso
from .serializers import (
    CursoSerializer,
    InscripcionCursoSerializer,
    UsuarioParaInscripcionSerializer,
)


User = get_user_model()


class CursoViewSet(viewsets.ModelViewSet):
    """
    Cursos del sistema.

    Admin:
    - Puede ver todos los cursos.
    - Puede crear, editar y eliminar cursos.

    Estudiante:
    - Solo puede ver cursos donde está inscrito.
    - No puede crear, editar ni eliminar.
    """

    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Curso.objects.all().order_by("id")

        return Curso.objects.filter(
            inscripciones__usuario=user,
            inscripciones__activa=True
        ).distinct().order_by("id")

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminRole()]
        return [IsAuthenticated()]


class InscripcionCursoViewSet(viewsets.ModelViewSet):
    """
    Permite al admin inscribir estudiantes a cursos.
    """

    queryset = InscripcionCurso.objects.select_related("usuario", "curso").all().order_by("id")
    serializer_class = InscripcionCursoSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]


class UsuariosParaInscripcionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lista usuarios disponibles para inscripción.
    Se excluyen administradores para que solo se inscriban estudiantes.
    """

    serializer_class = UsuarioParaInscripcionSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get_queryset(self):
        return User.objects.filter(
            is_staff=False,
            is_superuser=False,
            is_active=True
        ).order_by("id")
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from plataforma_quimica.permissions import IsAdminRole
from .serializers import UsuarioSerializer, UsuarioListadoSerializer


User = get_user_model()


class CustomAuthToken(ObtainAuthToken):
    """
    Login personalizado.
    Devuelve token y datos del usuario, incluyendo rol.
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        rol = "admin" if user.is_staff or user.is_superuser else "estudiante"

        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
            "rol": rol,
        })


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    CRUD de usuarios.
    Solo administradores pueden listar, crear, editar o eliminar usuarios.
    """

    queryset = User.objects.all().order_by("id")
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get_serializer_class(self):
        if self.action == "list":
            return UsuarioListadoSerializer
        return UsuarioSerializer


class PerfilUsuarioAPIView(viewsets.ReadOnlyModelViewSet):
    """
    Permite consultar información básica del usuario autenticado.
    """

    serializer_class = UsuarioListadoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
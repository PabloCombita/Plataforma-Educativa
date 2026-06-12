from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomAuthToken, UsuarioViewSet, PerfilUsuarioAPIView


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'perfil', PerfilUsuarioAPIView, basename='perfil')


urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login-token'),
    path('', include(router.urls)),
]
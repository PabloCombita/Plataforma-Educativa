from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CursoViewSet,
    InscripcionCursoViewSet,
    UsuariosParaInscripcionViewSet,
)


router = DefaultRouter()
router.register(r'cursos', CursoViewSet, basename='cursos')
router.register(r'inscripciones', InscripcionCursoViewSet, basename='inscripciones')
router.register(r'estudiantes-disponibles', UsuariosParaInscripcionViewSet, basename='estudiantes-disponibles')


urlpatterns = [
    path('', include(router.urls)),
]
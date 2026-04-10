from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluacionViewSet, IntentoEvaluacionAPIView, ProgresoAPIView

router = DefaultRouter()
router.register(r'evaluaciones', EvaluacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('responder/', IntentoEvaluacionAPIView.as_view()),
    path('progreso/<int:curso_id>/', ProgresoAPIView.as_view()),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeccionViewSet

router = DefaultRouter()
router.register(r'lecciones', LeccionViewSet, basename='leccion')

urlpatterns = router.urls
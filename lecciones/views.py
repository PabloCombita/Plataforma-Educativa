from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Leccion
from .serializers import LeccionSerializer

class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer
    permission_classes = [IsAuthenticated]
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Evaluacion, IntentoEvaluacion
from .serializers import EvaluacionSerializer

class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
    permission_classes = [IsAuthenticated]

class IntentoEvaluacionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        evaluacion_id = request.data.get('evaluacion')
        respuesta_usuario = request.data.get('respuesta')

        try:
            evaluacion = Evaluacion.objects.get(id=evaluacion_id)
        except Evaluacion.DoesNotExist:
            return Response(
                {"error": "Evaluación no existe"},
                status=status.HTTP_404_NOT_FOUND
            )

        es_correcta = evaluacion.respuesta_correcta == respuesta_usuario

        IntentoEvaluacion.objects.create(
            usuario=request.user,
            evaluacion=evaluacion,
            respuesta=respuesta_usuario,
            es_correcta=es_correcta
        )

        return Response(
            {
                "correcta": es_correcta,
                "mensaje": "Respuesta correcta" if es_correcta else "Respuesta incorrecta"
            },
            status=status.HTTP_201_CREATED
        )

class ProgresoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, curso_id):
        total = Evaluacion.objects.filter(
            leccion__curso_id=curso_id
        ).count()

        correctas = IntentoEvaluacion.objects.filter(
            usuario=request.user,
            evaluacion__leccion__curso_id=curso_id,
            es_correcta=True
        ).count()

        porcentaje = (correctas / total * 100) if total > 0 else 0

        return Response({
            "curso": curso_id,
            "progreso": porcentaje
        })
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from plataforma_quimica.permissions import IsAdminRole
from .models import Evaluacion, IntentoEvaluacion
from .serializers import EvaluacionSerializer


class EvaluacionViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        queryset = Evaluacion.objects.select_related(
            "leccion",
            "leccion__curso"
        ).all().order_by("leccion__curso_id", "leccion_id", "id")

        curso_id = self.request.query_params.get("curso")
        leccion_id = self.request.query_params.get("leccion")

        if curso_id:
            queryset = queryset.filter(leccion__curso_id=curso_id)

        if leccion_id:
            queryset = queryset.filter(leccion_id=leccion_id)

        if user.is_staff or user.is_superuser:
            return queryset

        return queryset.filter(
            leccion__curso__inscripciones__usuario=user,
            leccion__curso__inscripciones__activa=True
        ).distinct()

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminRole()]
        return [IsAuthenticated()]


class IntentoEvaluacionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        evaluacion_id = request.data.get("evaluacion")
        respuesta_usuario = request.data.get("respuesta")

        if not evaluacion_id:
            return Response(
                {"error": "Debe enviar el ID de la evaluación."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not respuesta_usuario:
            return Response(
                {"error": "Debe enviar una respuesta."},
                status=status.HTTP_400_BAD_REQUEST
            )

        respuesta_usuario = str(respuesta_usuario).upper().strip()

        if respuesta_usuario not in ["A", "B", "C"]:
            return Response(
                {"error": "La respuesta debe ser A, B o C."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            evaluacion = Evaluacion.objects.select_related(
                "leccion",
                "leccion__curso"
            ).get(id=evaluacion_id)
        except Evaluacion.DoesNotExist:
            return Response(
                {"error": "La evaluación no existe."},
                status=status.HTTP_404_NOT_FOUND
            )

        user = request.user

        if not (user.is_staff or user.is_superuser):
            esta_inscrito = evaluacion.leccion.curso.inscripciones.filter(
                usuario=user,
                activa=True
            ).exists()

            if not esta_inscrito:
                return Response(
                    {"error": "No estás inscrito en el curso de esta evaluación."},
                    status=status.HTTP_403_FORBIDDEN
                )

        respuesta_correcta = str(evaluacion.respuesta_correcta).upper().strip()
        es_correcta = respuesta_correcta == respuesta_usuario

        IntentoEvaluacion.objects.create(
            usuario=user,
            evaluacion=evaluacion,
            respuesta=respuesta_usuario,
            es_correcta=es_correcta
        )

        return Response(
            {
                "correcta": es_correcta,
                "mensaje": "Respuesta correcta" if es_correcta else "Respuesta incorrecta",
                "respuesta_enviada": respuesta_usuario,
                "respuesta_correcta": respuesta_correcta,
            },
            status=status.HTTP_201_CREATED
        )


class ProgresoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, curso_id):
        user = request.user

        total_evaluaciones = Evaluacion.objects.filter(
            leccion__curso_id=curso_id
        ).count()

        evaluaciones_correctas = IntentoEvaluacion.objects.filter(
            usuario=user,
            evaluacion__leccion__curso_id=curso_id,
            es_correcta=True
        ).values_list(
            "evaluacion_id",
            flat=True
        ).distinct()

        correctas = evaluaciones_correctas.count()

        if total_evaluaciones == 0:
            progreso = 0
        else:
            progreso = round((correctas / total_evaluaciones) * 100, 2)

        return Response({
            "curso": curso_id,
            "total_evaluaciones": total_evaluaciones,
            "correctas": correctas,
            "progreso": progreso
        })
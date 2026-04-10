from rest_framework import serializers
from .models import Evaluacion, IntentoEvaluacion

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'

class IntentoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntentoEvaluacion
        fields = '__all__'


from rest_framework import serializers
from .models import Deslizamiento, DeslizamientosMonitoreados, FincasCafeterasMonitoreadas, DeslizamientosReportados

class DeslizamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Deslizamiento
        fields = "__all__"


class DeslizamientoMonitoreadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeslizamientosMonitoreados
        fields = "__all__"


class FincaCafeteraMonitoreadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FincasCafeterasMonitoreadas
        fields = "__all__"


class DeslizamientosReportadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeslizamientosReportados
        fields = "__all__"
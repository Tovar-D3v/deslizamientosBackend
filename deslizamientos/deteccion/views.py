from rest_framework import viewsets
from .models import Deslizamiento, DeslizamientosMonitoreados, FincasCafeterasMonitoreadas
from .serializers import DeslizamientoSerializer, DeslizamientoMonitoreadoSerializer, FincaCafeteraMonitoreadaSerializer

class DeslizamientoViewSet(viewsets.ModelViewSet):
    queryset         = Deslizamiento.objects.all().order_by('-fecha')
    serializer_class = DeslizamientoSerializer


class DeslizamientosMonitoreadosViewSet(viewsets.ModelViewSet):
    queryset = DeslizamientosMonitoreados.objects.all().order_by("-id")
    serializer_class = DeslizamientoMonitoreadoSerializer
    
    
class FincasCafeterasMonitoreadasViewSet(viewsets.ModelViewSet):
    queryset = FincasCafeterasMonitoreadas.objects.all().order_by("-id")
    serializer_class = FincaCafeteraMonitoreadaSerializer
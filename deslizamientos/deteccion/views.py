from rest_framework import viewsets
from .models import Deslizamiento, DeslizamientosMonitoreados, FincasCafeterasMonitoreadas
from .serializers import DeslizamientoSerializer, DeslizamientoMonitoreadoSerializer, FincaCafeteraMonitoreadaSerializer
from django.contrib.gis.geos import Polygon

class DeslizamientoViewSet(viewsets.ModelViewSet):
    serializer_class = DeslizamientoSerializer

    def get_queryset(self):
        queryset = Deslizamiento.objects.all()
        # Obtener los parámetros de los límites (bound box) del mapa
        # Ejemplo: ?bbox=min_lon,min_lat,max_lon,max_lat
        bbox_str = self.request.query_params.get('bbox')

        if bbox_str:
            try:
                min_lon, min_lat, max_lon, max_lat = map(float, bbox_str.split(','))
                
                # Filtrar por rangos de latitud y longitud
                queryset = queryset.filter(
                    longitud__gte=min_lon,  # longitud Greater Than or Equal
                    longitud__lte=max_lon,  # longitud Less Than or Equal
                    latitud__gte=min_lat,   # latitud Greater Than or Equal
                    latitud__lte=max_lat    # latitud Less Than or Equal
                )
            except ValueError:
                pass # Manejar errores si el bbox es inválido

        # Puedes combinarlo con la paginación si lo deseas
        return queryset.order_by('-id')

class DeslizamientosMonitoreadosViewSet(viewsets.ModelViewSet):
    queryset = DeslizamientosMonitoreados.objects.all().order_by("nombre")
    serializer_class = DeslizamientoMonitoreadoSerializer


class FincasCafeterasMonitoreadasViewSet(viewsets.ModelViewSet):
    queryset = FincasCafeterasMonitoreadas.objects.all().order_by("nombre_finca")
    serializer_class = FincaCafeteraMonitoreadaSerializer

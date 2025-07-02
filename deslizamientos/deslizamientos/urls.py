from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from deteccion.views import DeslizamientoViewSet, DeslizamientosMonitoreadosViewSet, FincasCafeterasMonitoreadasViewSet

router = DefaultRouter()
router.register(r'deslizamientos', DeslizamientoViewSet, basename='deslizamientos')
router.register(r"monitoreados", DeslizamientosMonitoreadosViewSet, basename="monitoreados")
router.register(r"fincas", FincasCafeterasMonitoreadasViewSet, basename="fincas_cafeteras")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

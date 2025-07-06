from django.contrib.gis.db import models
from django.utils import timezone

class Deslizamiento(models.Model):
    # Volvemos a las columnas separadas
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    
    # Mantenemos los otros campos
    deslizamiento_prediccion = models.BooleanField(default=False, null=True, blank=True)
    deslizamiento_real = models.BooleanField(default=False, null=True, blank=True)
    fecha_deslizamiento_prediccion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_deslizamiento_real = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class DeslizamientosMonitoreados(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    norte  = models.FloatField()
    sur    = models.FloatField()
    este   = models.FloatField()
    oeste  = models.FloatField()
    nivel_movimiento = models.FloatField()
    activo = models.BooleanField(default=True)
    icono = models.CharField(max_length=100, default='signal')

class FincasCafeterasMonitoreadas(models.Model):
    codigo_municipio = models.CharField(max_length=10, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    lista = models.CharField(max_length=100, null=True, blank=True)
    nombre_vereda = models.CharField(max_length=100, null=True, blank=True)
    nombre_finca = models.CharField(max_length=100, null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    estado_finca = models.CharField(max_length=50, null=True, blank=True)
    area_total = models.FloatField(null=True, blank=True)
    area_cafe = models.FloatField(null=True, blank=True)
    luminosidad = models.CharField(max_length=50, null=True, blank=True)


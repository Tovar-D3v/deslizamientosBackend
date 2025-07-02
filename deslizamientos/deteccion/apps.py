from django.apps import AppConfig

class DeteccionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "deteccion"

    def ready(self):
        import deteccion.signals  # activa los handlers de señal aquí

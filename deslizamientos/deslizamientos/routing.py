from django.urls import re_path
from deteccion.consumers import DeslizamientoConsumer

websocket_urlpatterns = [
    re_path(r"^ws/deslizamientos/$", DeslizamientoConsumer.as_asgi()),
]

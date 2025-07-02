import os

# 1) Define tus settings antes de todo
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deslizamientos.settings")

# 2) Importar y arrancar el setup de Django
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

# 3) Channels
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import deslizamientos.routing  # tu routing de WS

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(deslizamientos.routing.websocket_urlpatterns)
    ),
})

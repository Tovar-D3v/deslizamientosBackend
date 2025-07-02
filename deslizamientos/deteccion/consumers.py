import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import DeslizamientosMonitoreados
from .serializers import DeslizamientoMonitoreadoSerializer

class DeslizamientoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 1) Únete al grupo
        self.group_name = "deslizamientos_group"
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        # 2) Acepta la conexión WebSocket
        await self.accept()

        # 3) Envía payload inicial con todos los registros
        registros = await sync_to_async(list)(
            DeslizamientosMonitoreados.objects.all()
        )
        data = DeslizamientoMonitoreadoSerializer(registros, many=True).data
        await self.send(text_data=json.dumps({
            "type": "initial",
            "data": data
        }))

    async def disconnect(self, close_code):
        # Al desconectar, salir del grupo
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Este método maneja los eventos enviados por el signal (group_send)
    async def deslizamiento_update(self, event):
        # event["data"] ya es el dict serializado
        await self.send(text_data=json.dumps({
            "type": "update",
            "data": event["data"]
        }))

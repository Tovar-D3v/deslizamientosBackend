from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import DeslizamientosMonitoreados
from .serializers import DeslizamientoMonitoreadoSerializer

@receiver(post_save, sender=DeslizamientosMonitoreados)
def broadcast_deslizamiento(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    data = DeslizamientoMonitoreadoSerializer(instance).data

    async_to_sync(channel_layer.group_send)(
        "deslizamientos_group",
        {
            "type": "deslizamiento_update",  # coincide con el consumer
            "data": data,
        }
    )

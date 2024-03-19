"""
ASGI config for WebSoketProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebSoketProject.settings')

from channels.routing import ProtocolTypeRouter,URLRouter

from  chat.routing import websocket_urlpatterns
import chat.routing
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat import consumers
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
        chat.routing.websocket_urlpatterns
        # path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
    )
    )
})


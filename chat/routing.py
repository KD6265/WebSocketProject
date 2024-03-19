from django.urls import path,include
from . import consumers
websocket_urlpatterns = [
    path('ws/sc/<str:groupName>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/asc/<str:groupName>/',consumers.MyAsyncConsumer.as_asgi()),
]

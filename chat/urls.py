from django.urls import path,include
from . import views

app_name = 'chat'
urlpatterns = [
    path('<str:group_name>/',views.chatRoom,name='chatRoom'),
    path('',views.index,name='index'),
]

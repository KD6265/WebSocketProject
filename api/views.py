from django.shortcuts import render
from chat.models import Chat
from chat.models import Group as ChatGroup
# Create your views here.
from django.contrib.auth.models import Group
from  account.models import CustomUser
from rest_framework import permissions,viewsets
from .serializer import GroupSerializer, UserSerializer,ChatSerializer,ChatGroupSerializer




class ChatGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Chat.objects.all().order_by('-date_joined')
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class ChatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Chat.objects.all().order_by('-date_joined')
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
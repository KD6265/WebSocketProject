from django.contrib.auth.models import Group
from  account.models import CustomUser
from chat.models import Group as ChatGroup

from rest_framework import serializers
from chat.models import Chat

class ChatGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatGroup
        # fields = ['url', 'username', 'email', 'groups']
        fields ='__all__'


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'  
        # fields = ['id',  'timestamp', 'group']  

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
        
    
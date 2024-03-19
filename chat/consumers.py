from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import sync_to_async
import json
from .models import Chat, Group
from channels.auth import login
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

class MyAsyncConsumer(AsyncConsumer):
    active_users = {}
    async def websocket_connect(self, event):
        print('websocket_connected ...', event)
        print('channel layer...', self.channel_layer)
        print('channel name...', self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupName']
        print('Group Name : ', self.group_name)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.send({
            'type': 'websocket.accept',
        })
        user = self.scope['user']
        print('User type: ', type(user))
        print('User_name: %s' % user)
        
    async def websocket_receive(self, event):
        print('message received from client', event)
        message = event['text']
        print(type(message))
        print(message)
        data = json.loads(message)
        print('data in python object', data)
        print(type(data))
        group = await sync_to_async(Group.objects.get)(name=self.group_name) 
        await login(self.scope, self.scope['user'])
        
        # await database_sync_to_async(self.scope["session"].save)()
        if self.scope['user'].is_authenticated:
            user = self.scope['user']
            # send to only this room/group if the user is authenticated else broadcast it to all users
            chat = Chat(content=data['msg'], group=group,user=user)
            await sync_to_async(chat.save)()    
            user = self.scope['user'].username
            profile_image = self.scope['user'].profile_image.url
            user_id = self.scope['user'].id
            data['user'] = user
            data['profile_image'] = profile_image
            print('data with user', data)
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message': json.dumps(data)
                }
            )
            print('Sent to client')
        else:
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({'msg': 'login required'}),
            })
        
    async def chat_message(self, event):
        print('chat message called', event)
        msg = event['message']
        print(msg)
        print(type(msg))
        await self.send({
            'type': 'websocket.send',
            'text': msg,
        })
        
    async def websocket_disconnect(self, event):
        # Notify anyone listening for this disconnection
        print('websocket disconnected....', event)
        print('channel layer...', self.channel_layer)
        print('channel name...', self.channel_name)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()
    
    # FOR ACTIVE USERS
    
    async def join_group(self, group_name, user_id):
        if group_name not in self.active_users:
            self.active_users[group_name] = []
        self.active_users[group_name].append(user_id)
        await self.broadcast_active_users(group_name)

    async def leave_group(self, group_name, user_id):
        if group_name in self.active_users and user_id in self.active_users[group_name]:
            self.active_users[group_name].remove(user_id)
            await self.broadcast_active_users(group_name)

    async def broadcast_active_users(self, group_name):
        active_users_data = self.active_users.get(group_name, [])
        await self.channel_layer.group_send(
            group_name,
            {
                'type': 'active_users.update',
                'active_users': active_users_data,
            }
        )

    async def active_users_update(self, event):
        active_users_data = event['active_users']
        print('Active users', active_users_data)
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps({'active_users': active_users_data}),
        })




















from  channels.consumer import  AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Chat,Group
# from channels.db import 
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket_connected ...', event)
        print('channel layer...',self.channel_layer)
        print('channel name...',self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupName']
        print('Group Name : ',self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.send({
            'type':'websocket.accept',
            })
        user = self.scope['user']
        print('User type: ',type(user))
        print('User_name: %s' % user)
        
    def websocket_receive(self,event):
        print('message received from client', event)
        message = event['text']
        print(type(message))
        print (message)
        data = json.loads(message)
        print('data in python object', data)
        print(type(data))
        group = Group.objects.get(name=self.group_name) 
        if self.scope['user'].is_authenticated:
            # send to only this room/group  if the user is authenticated else broadcast it to all users
            chat  =  Chat(content = data['msg'], group = group )
            chat.save()
            user = self.scope['user'].username
            user_id = self.scope['user'].id
            # print('auth user:' , user,user_id)
            data['user'] = user
            print ('data with user',data)
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type':'chat.message',
                    'message': json.dumps(data)
                }
            )
            # print("Sent to group")
            print('Sent to clint')
        else:
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({'msg':'login required'}),
                })        
    def chat_message(self,event):
        print('chat message called',event)
        msg = event['message']
        print(msg)
        print(type(msg))
        self.send({
            'type': 'websocket.send',
            'text': msg,
            })  
        
        
        
    def websocket_disconnect(self,event):
        # Notify anyone listening for this disconnection
        print('websocket disconnected....', event)
        print('channel layer...',self.channel_layer)
        print('channel name...',self.channel_name)
        self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()


# from channels.generic.websocket import WebsocketConsumer

# class MySyncConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         # Handle received data
#         pass
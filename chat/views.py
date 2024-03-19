from django.shortcuts import render
from .models  import Group,Chat
from django.contrib.auth.decorators import login_required
import qr_code
from qrcode import make
@login_required
def index(request,group_name):
    print(request)
    
    # GENERATE qr CODE FOR  GROUP
    baseurl = request.build_absolute_uri()
    
    print('baseurl : ',baseurl)
    print('Group Name: ' + group_name)
    group = Group.objects.filter(name=group_name).first()
    print('Group',group)
    chats=[]
    if group is None:
        group = Group.objects.create(name=group_name)
    else:
        chats = Chat.objects.filter(group=group)
        print('chats in view ....',chats)
    return render(request, 'chat\index.html', {'group_name': group_name, 'group': group,'messages': chats,'baseurl': baseurl,'img':'msg'})
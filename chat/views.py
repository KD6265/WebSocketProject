from django.shortcuts import render ,redirect
from .models  import Group,Chat
from django.contrib.auth.decorators import login_required
from .permission_handlers import user_is_authenticated_and_active
from .forms import GroupForm
import qr_code
from qrcode import make


def index(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return redirect('chat',name=name)

    form = GroupForm()
    group_lists = Group.objects.filter(created_by=request.user.profile)
    return render(request,'chat/index.html', {'group_lists': group_lists,'form': form,},)
    

@user_is_authenticated_and_active
def chatRoom(request,group_name):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return redirect('chat',name=name)
    print(request)
    baseurl = request.build_absolute_uri()
    print('baseurl : ',baseurl)
    print('Group Name: ' + group_name)
    group = Group.objects.filter(name=group_name).first()
    print('Group',group)
    chats=[]
    if group is None:
        group = Group.objects.create(name=group_name,created_by=request.user.profile)
    else:
        chats = Chat.objects.filter(group=group)
        print('chats in view ....',chats)
    form = GroupForm()
    group_lists = Group.objects.filter(created_by=request.user.profile)
    return render(request, 'chat\chat.html', {'group_name': group_name, 'group': group,'messages': chats,'baseurl': baseurl,'img':'msg','group_lists': group_lists,'form': form,})
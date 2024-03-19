from django.shortcuts import render 
from django.http import HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from chat.forms import GroupForm
from chat.models import Group
# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES) # instance=request.user
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('username: ', username)
            print('passwd : ', password)
            print('user : ', user)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        print('get req call ')
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



# def dashboard(request):
#     # if request.method == 'POST':
#     #     form = GroupForm(request,request.POST)
#     #     print('post req call ',request.POST)
#     #     if form.is_valid():
#     #         print('form valid call ')
#     #         group_name = request.POST.get('name')
#     #         print('Group Name : ',group_name)
#     #         new_group =  Group(name=group_name)
#     #         group = new_group.save()
            
#     #         # group = form.save(commit=False)
#     #         # group.owner = request.user
#     #         # group.save()
#     #         messages.success(request,f" {group} Group created successfully!{group}")
#     #         return HttpResponseRedirect('index'+str(group.name))
#     # else:
#     #     form = GroupForm()
#     # Add dashboard logic here
#     form = GroupForm()
#     return render(request, 'account/dashboard.html', {'form': form})

def dashboard(request):
    form = GroupForm()
    baseurl = request.build_absolute_uri()
    print('dashboard baseur ', baseurl)
    return render(request, 'account/dashboard.html', {'form': form})

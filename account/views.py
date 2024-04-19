from django.shortcuts import render 
from django.http import HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from chat.forms import GroupForm
from chat.models import Group,Chat
from django.db.models import Count


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from pricing.models import  PlanPrice,Plan
from  account.models import CustomUser,UserProfile

def index(request):
    plan = Plan.objects.filter(active=True)
    return render(request, 'index.html', {'plans': plan})


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
                UserProfile.update_user_profile_status(user.profile)
                return redirect('dashboard')
    else:
        print('get req call ')
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    form = GroupForm()
    baseurl = request.build_absolute_uri()
    from django.db.models import Count

    group_count = Group.objects.filter(created_by=request.user.profile).count()

    print('group count : ' ,group_count)
    print('dashboard baseur ', baseurl)
    return render(request, 'account/dashboard.html', {'form': form})

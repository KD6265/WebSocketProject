from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser
from  django.contrib import messages
from chat.models import Group
def user_is_authenticated_and_active(function):
    """Decorator for checking if user is authenticated and profile is active"""
    def wrap(request, *args, **kwargs):
        user = request.user
        group_name = kwargs.get('group_name')
        group_author = None
        
        if Group.objects.filter(name=group_name).exists():
            group_author = Group.objects.get(name=group_name).created_by
            print('group author:', group_author)
        
        print("user:", user)
        print(str(user) != str(group_author))
        
        if isinstance(user, AnonymousUser):
            return function(request, *args, **kwargs)
        elif not user.is_authenticated:
            messages.error(request, 'Please login first')
            return redirect('login')
        elif not user.profile.active:
            messages.error(request, 'Your Plan is not active. Please first upgrade your plan')
            return redirect("dashboard")
        elif user.profile.selected_plan.chat_room_limit == 0:
            messages.info(request, 'You have successfully joined the group.')
            return function(request, *args, **kwargs)
        elif user.profile.selected_plan.chat_room_limit <= user.profile.created_by.count() :
            if str(user) != str(group_author):
                messages.error(request, 'You have reached your chat room limit. Upgrade your plan or join your own room.')
                return redirect("dashboard")
            else:    
                messages.success(request, 'You have successfully joined the group.')
                messages.info(request, 'You have reached your chat room limit.')
                
                return function(request, *args, **kwargs)
        else:
            messages.info(request, 'You have successfully joined the group.')
            return function(request, *args, **kwargs)
    return wrap

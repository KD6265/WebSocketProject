from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser
from  django.contrib import messages

def user_is_authenticated_and_active(function):
    """Decorator for checking if user is authenticated and profile is active
    """
    def wrap(request, *args, **kwargs):
        user = request.user
        if isinstance(user, AnonymousUser):
            return function(request, *args, **kwargs)
        elif not user.is_authenticated:
            messages.error(request, 'Please login first')
            return redirect('login')
        elif not user.profile.active:
            messages.error(request, 'Your Plan is not active. please first upgrade your plan')
            return redirect("dashboard")
        else:
            return function(request, *args, **kwargs)
    return wrap
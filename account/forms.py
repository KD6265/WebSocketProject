# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
class SignUpForm(UserCreationForm):
    profile_image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2','profile_image')

class LoginForm(AuthenticationForm):
    # Add custom fields if needed
    pass

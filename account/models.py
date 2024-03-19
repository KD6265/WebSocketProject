from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/',default='download_1.jpg', null=True, blank=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional profile fields

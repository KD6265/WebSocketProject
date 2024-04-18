from  django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserProfile, CustomUser
from django.contrib import messages

# #  profile create signal
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # user =instance.user.save()
        # request = kwargs.get('request')
        # msg = 'Your account has been created! You are now able to log in'
        profile = UserProfile.objects.create(user = instance)
        # messages.success(request, f'Your account has been created! You are now able to log in') 
        # print("msg", msg)


#  Zxcv@12345

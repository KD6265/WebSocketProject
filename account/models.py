from django.db import models
from django.contrib.auth.models import AbstractUser
from  pricing.models  import Plan
from dateutil.relativedelta import relativedelta

from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/',default='download_1.jpg', null=True, blank=True)    
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name="profile")
    selected_plan = models.ForeignKey(Plan,on_delete=models.CASCADE, null=True, blank=True,related_name="selected_plan")
    active = models.BooleanField(default=False)
    end_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}'
    @property
    def remain_time(self):
        now = timezone.now()
        if self.end_date is None:
            return 0
        remaining_days = (self.end_date - now).days
        return remaining_days if remaining_days > 0 else 0
    @property
    def remain_chat_room_limit(self):
        if self.selected_plan is None:  
            return 0    
        else:
            return self.selected_plan.chat_room_limit - self.user.chat_rooms.count()
        
    def update_user_profile_status(self):
        if self.remain_time is not None:
            remaining_days = self.remain_time
            print('remaining days: ', remaining_days)
            if remaining_days <= 0:
                self.active = False
                UserProfile.objects.filter(pk=self.pk).update(active=False)
                

    def save(self, *args, **kwargs):
        # self.end_date = timezone.now() + relativedelta(months=self.selected_plan.duration)
        self.update_user_profile_status()
        super(UserProfile, self).save(*args, **kwargs)
    

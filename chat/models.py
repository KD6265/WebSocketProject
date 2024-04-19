from django.db import models
from django.contrib.auth.models import User
from account.models import CustomUser,UserProfile
# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='chat_rooms')
    document = models.FileField(upload_to='documents/',blank=True,null=True)
    content  = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE,related_name="chat_group")
    upload = models.FileField(blank=True, null=True, upload_to='uploads/'),
    def __str__(self):
        return self.content[:50] + '...' if len(self.content) > 53 else self.content

class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    topic = models.TextField(blank=True)
    group_icon = models.ImageField(upload_to='group_icons/', blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE,default=1,related_name="created_by")
    # users = models.ManyToManyField(UserProfile, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def created_by(self,obj):
    #     return obj.chat_group.first().user if obj.chat_group.exists() else None
    # # created_by.short_description = 'Created By'
    
    def __str__(self) -> str:
        return self.name


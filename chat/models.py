from django.db import models
from django.contrib.auth.models import User
from account.models import CustomUser
# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/',blank=True,null=True)
    content  = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE,)
    upload = models.FileField(blank=True, null=True, upload_to='uploads/'),
    def __str__(self):
        return self.content[:50] + '...' if len(self.content) > 53 else self.content

class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)


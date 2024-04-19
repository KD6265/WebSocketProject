from django.db import models
from django.utils import timezone


# Create your models here.
from datetime import timedelta

class Plan(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False,help_text="plan name")
    description = models.TextField(blank=True,null=True,max_length=200) 
    price = models.IntegerField()
    duration = models.IntegerField(help_text="duration in months",default=1)
    chat_room_limit = models.PositiveIntegerField(default=0,help_text="0 for unlimited rooms")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"
        

class Feature(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="features",default=1)
    name = models.CharField(max_length=100, blank=False, null=False,help_text="feature name")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

class PlanPrice(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="prices",)
    currency =  models.CharField(choices=[('INR','INR'),('USD','USD')],max_length=10,default='INR')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.plan)
    @property
    def get_price(self):
        return self.plan.price
    
    class Meta:
        verbose_name = "PlanPrice"
        verbose_name_plural = "PlanPrices"
                
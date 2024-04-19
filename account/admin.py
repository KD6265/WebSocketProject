from django.contrib import admin
from .models import CustomUser ,UserProfile
from pricing.models import Plan,PlanPrice
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display =['id','username','email','profile_image']

class UserProfileAdmin(admin.ModelAdmin):
    list_display =['id','user','selected_plan','active','remain_chat_room_limit','remain_day','end_date', 'created_at','updated_at',] 
    list_filter = ['user']
    search_fields = ['user']
    
    def remain_day(self,obj):
        return obj.remain_time
    remain_day.sort_deshort_description = " days remaining"

    def remain_chat_room_limit(self,obj):
        return obj.remain_chat_room_limit
    remain_chat_room_limit.sort_deshort_description = " chat room limit"

    
admin.site.register(UserProfile,UserProfileAdmin)

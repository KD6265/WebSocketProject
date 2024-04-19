from django.contrib import admin
from .models import  Chat,Group
# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display =['id' ,'content','timestamp','group','created_by']
    list_filter = ('user', 'group')  
    search_fields = ('content',) 

    def created_by(self,obj):
        return obj.user
    created_by.short_description = 'Created By'

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name','topic','created_by','group_icon','created_at']

    # def created_by(self,obj):
    #     return obj.chat_group.first().user if obj.chat_group.exists() else None
    # created_by.short_description = 'Created By'
    
    
# admin.site.register(Chat,ChatAdmin)
# admin.site.register(GroupAdmin,Group)
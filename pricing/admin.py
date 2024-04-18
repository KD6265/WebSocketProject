from django.contrib import admin

# Register your models here.
from .models import Plan,PlanPrice,Feature


class FeatureAdmin(admin.StackedInline):
    model = Feature



class PlanAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','duration','active','created_at','updated_at')
    list_filter = ('name','description','price','duration','created_at','updated_at')
    # inlines = (FeatureAdmin,)
admin.site.register(Plan,PlanAdmin)

class PlanPriceAdmin(admin.ModelAdmin):
    list_display = ('plan','currency','created_at','updated_at')
    list_filter = ('plan','currency','created_at','updated_at')
admin.site.register(PlanPrice,PlanPriceAdmin)


# urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('purchase_plan/<int:plan_id>/', views.purchase_plan, name='purchase_plan'),
]

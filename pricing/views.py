from django.shortcuts import render ,redirect
from django.http import HttpResponse
from  .models import Plan,PlanPrice
from django.contrib.auth.decorators import login_required
from  account.models import UserProfile
from  django.utils  import timezone
from django.contrib import messages
from dateutil.relativedelta import relativedelta
# Create your views here.
@login_required(login_url='login')
def purchase_plan(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    if plan is  not None:
        user = request.user
        print(user)
        userProfile = UserProfile.objects.get(user=user)
        userProfile.selected_plan = plan
        userProfile.active = True
        userProfile.end_date = timezone.now() + relativedelta(months=plan.duration)
        userProfile.save()
        msg = f'plan {plan.name} purchased successfully'
        messages.success(request,msg)
        return redirect('dashboard')
    else:
        return HttpResponse('plan not found')


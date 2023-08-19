from django.shortcuts import redirect, render,get_object_or_404
from django.utils import timezone
from .models import Fund 

def index(request):
    if request.method == "POST":
        new_fund=Fund(
                title=request.POST.get("title"),
                content=request.POST.get("description"),
                goal=request.POST.get("goal"),
                event_datetime=timezone.now()
                )
        new_fund.save()
        return redirect("cf-home")
    return render(request,"crowdFunding/index.html")

def details(request,slug):
    fund = get_object_or_404(Fund, slug=slug)
    if request.method == "POST":        
        donation=int(request.POST.get("donation"))
        fund.amount_gained += donation
        fund.save()
        return redirect("cf-details",slug=slug)

    return render(request, 'crowdFunding/details.html', {'fund': fund})



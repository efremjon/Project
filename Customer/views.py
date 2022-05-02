from django.shortcuts import render

# Create your views here.


def Customer_dashboard(request):
    return render(request,'Customer/Customer_dashbord.html',{})
    

from django.shortcuts import render

# Create your views here.

def Agent_dashboard(request):
    return render(request,'Agent/agent-dashboard.html',{})

def customer_order(request):
     return render(request,'Agent/view-cust-orders.html',{})

    
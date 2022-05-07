from django.shortcuts import render

# Create your views here.

def Agent_dashboard(request):
    return render(request,'Agent/agent-dashboard.html',{})

def customer_order(request):
     return render(request,'Agent/view-cust-orders.html',{})
     
def make_order(request):
     return render(request,'Agent/make-order.html',{})

def manage_customers(request):
     return render(request,'Agent/manage-customers.html',{})

   

def manage_drivers(request):
     return render(request,'Agent/manage-drivers.html',{})



def transactions(request):
     return render(request,'Agent/transactions.html',{})


def send_message(request):
     return render(request,'Agent/send-message.html',{})



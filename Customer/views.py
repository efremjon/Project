from django.shortcuts import render

# Create your views here.


def Customer_dashboard(request):
    return render(request,'Customer/home.html')
    
def make_order(request):
    return render(request,'Customer/make_ordera.html')

def send_delivery(request):
    return render(request,'Customer/send-delivery-status.html')

def transaction_history(request):
    return render(request,'Customer/transaction_history.html')
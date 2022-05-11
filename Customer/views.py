from http.client import CONTINUE
from multiprocessing import context
from multiprocessing.dummy import JoinableQueue
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import PasswordChangeForm
from Agent.models import Customer
from .form import passwordform
from django.core.mail import send_mail

from django.shortcuts import render

# Create your views here.


def Customer_dashboard(request):
    return render(request,'Customer/Customer_home_page.html')
    
# User Profile
def show_profile(request):
    return render(request,'Customer/profile/show_profile.html',)

def edit_profile(request):
    return render(request,'Customer/profile/edit_profile.html',)


def change_password(request):
    users=User.objects.get(id=request.user.id)
    admin=users.customer
    
    if request.method == 'POST':
        form = passwordform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('show_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = passwordform(request.user)
    context = {
        'admin':admin ,
        'usermodel':users,
        'form':form
    }
    return render(request, 'Customer/profile/chage_password.html', context)

def change_profile_pic(request):
    return render(request,'Customer/profile/edit_profile.html',)

def delete_profile_pic(request):
    return render(request,'Customer/profile/edit_profile.html',)

# end user profile




def make_order(request):
    return render(request,'Customer/customer_order.html')

def send_delivery(request):
    return render(request,'Customer/send-delivery-status.html')

def transaction_history(request):
    return render(request,'Customer/transaction_history.html')
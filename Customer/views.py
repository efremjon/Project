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
# from .form import passwordform,NameForm
from django.core.mail import send_mail

from django.shortcuts import render

# Create your views here.


def Customer_dashboard(request):
    return render(request,'Customer/home.html')
    
# User Profile
def show_profile(request):
    users=User.objects.get(id=request.user.id)
    admin=users.customer
    context = {
        'admin':admin ,
        
    }
    return render(request,'Customer/profile/show_profile.html',context)

def edit_profile(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    context = {
        'admin':admin ,
        
    }
    if request.method == 'POST':
        admin.about=request.POST['about']
        admin.phone1=request.POST['phone']
        admin.Company=request.POST['company']
        admin.Country=request.POST['country']
        admin.Job=request.POST['job']
        admin.address=request.POST['address']
        admin.facebook=request.POST['facebook']
        admin.telegram=request.POST['telegram']
        admin.instagram=request.POST['instagram']
        users.first_name=request.POST['first_name']
        users.last_name=request.POST['last_name']
        users.email=request.POST['email']
        admin.save()
        users.save()
        return redirect ('show_profile')
    return render(request,'Company/profile/edit_profile.html',context)

# def change_password(request):
#     users=User.objects.get(id=request.user.id)
#     admin=users.admin
    
#     if request.method == 'POST':
#         form = passwordform(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('show_profile')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = passwordform(request.user)
#     context = {
#         'admin':admin ,
#         'usermodel':users,
#         'form':form
#     }
#     return render(request, 'Company/profile/chage_password.html', context)

def change_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    context = {
        'admin':admin ,
        'usermodel':users
    }
    if request.method == 'POST':
        if len(request.FILES['img']) != 0:
            admin.profile_pic.delete()
            admin.profile_pic=request.FILES['img']
            admin.save()
            return redirect ('edit_profile')
        else:
            return render(request,'Company/profile/change_profile_pic.html',context)
    return render(request,'Company/profile/change_profile_pic.html',context)

def delete_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    context = {
        'admin':admin ,
        'usermodel':users
    }
    if len(admin.profile_pic) != 0:
        admin.profile_pic.delete()
        return redirect ('edit_profile')
    
    return render(request,'Company/profile/edit_profile.html',context)

# end user profile




def make_order(request):
    return render(request,'Customer/cust_order.html')

def send_delivery(request):
    return render(request,'Customer/send-delivery-status.html')

def transaction_history(request):
    return render(request,'Customer/transaction_history.html')
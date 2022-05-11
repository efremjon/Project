from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import PasswordChangeForm
from .form import *
from .models import *
from Company.models import Agent


# Create your views here.

def Agent_dashboard(request):

    return render(request,'Agent/agent-dashboard.html',{})

# user profile part

def show_profile(request):
    return render(request,'Agent/profile/show_profile.html')

def edit_profile(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
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
    return render(request,'Agent/profile/edit_profile.html',context)


def change_password(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
    
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
    return render(request, 'Agent/profile/chage_password.html', context)
def change_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
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
    return render(request,'Agent/profile/change_profile_pic.html',context)

def delete_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
    context = {
        'admin':admin ,
        'usermodel':users
    }
    if len(admin.profile_pic) != 0:
        admin.profile_pic.delete()
        return redirect ('edit_profile')
    
    return render(request,'Agent/profile/edit_profile.html',context)

# end user profile part





def customer_order(request):

     return render(request,'Agent/view-cust-orders.html',{})
     
def make_order(request):

     return render(request,'Agent/g.html',{})

def manage_customers(request):

     return render(request,'Agent/manage-customers.html',{})

   
def manage_drivers(request):

     return render(request,'Agent/manage-drivers.html',{})



def transactions(request):

     return render(request,'Agent/transactions.html',{})


def send_message(request):

     return render(request,'Agent/send-message.html',{})



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
from .models import *
from .form import passwordform,NameForm
from django.core.mail import send_mail

# Create your views here.

def Admin_dashboard(request):

    return render(request,'Company/admin.html',{})

def add_agent(request):
    form =NameForm()
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Full_Name=first_name+" " +last_name
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        phone1=request.POST['phone1']
        phone2=request.POST['phone2']
        facebook=request.POST['facebook']
        telegram=request.POST['telegram']
        instagram=request.POST['instagram']
        about=request.POST['about']
        profile_pic=request.FILES['img']
        city=request.POST['city']
        address=request.POST['address']
        location=request.POST['location']
        TIN_Num=request.POST['TIN_NO']
        agreement=request.FILES['agreement']
        licenc=request.FILES['licenc']
        form =NameForm(request.POST)
        region = form.cleaned_data['Region']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username taken')
                return render(request,'Company/add-agent.html',{})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken ')
                return render(request,'Company/add-agent.html',{})
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
                user.save()
                group = Group.objects.get(name='Agent')
                user.groups.add(group)
                Agent.objects.create(user=user,phone1=phone1,phone2=phone2,facebook=facebook,telegram=telegram,instagram=instagram, about=about,profile_pic=profile_pic,city=city,address=address,location=location,TIN_NO=TIN_Num,agreement=agreement,License=licenc,Full_Name=Full_Name,Region=region)
                messages.info(request, 'Sucssesfull Create User')
                return redirect ('/')
        else:
            messages.info(request, 'PASSWORD NOT MUCH')
            return render(request,'Company/add-agent.html',{})
    return render(request,'Company/add-agent.html',{'form':form})

def show_profile(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    context = {
        'admin':admin ,
        
    }

    return render(request,'Company/profile/show_profile.html',context)

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

def change_password(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    
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
    return render(request, 'Company/profile/chage_password.html', context)

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

def add_staff(request):
    return HttpResponse('staff removed')

def remove_staff(request):
    return HttpResponse('staff removed')

def remove_agent(request):
    return HttpResponse('agent removed')

def view_agent_orders(request):
    return HttpResponse('agent orders')

def approve_agent_orders(request):
    return HttpResponse('agent orders approved')

def store(request):
    return HttpResponse('store')


def contact_store_manager(request):
    return HttpResponse('contact store manager')

def agent_report(request):
    return HttpResponse('agent report')

def finance_report(request):
    return HttpResponse('finance report')


def advertisements(request):
    return HttpResponse('addvertisment')


def agent_view(request):
    return render(request,'Company/agent-view.html',{})

def agent_detail(request):
    return render(request,'Company/agent-detail.html',{})

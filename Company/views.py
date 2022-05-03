from multiprocessing.dummy import JoinableQueue
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import PasswordChangeForm
from .models import *

# Create your views here.

def Admin_dashboard(request):

    return render(request,'Company/admin.html',{})

def add_agent(request):

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
                Agent.objects.create(user=user,phone1=phone1,phone2=phone2,facebook=facebook,telegram=telegram,instagram=instagram, about=about,profile_pic=profile_pic,city=city,address=address,location=location,TIN_NO=TIN_Num,agreement=agreement,License=licenc,Full_Name=Full_Name)
                messages.info(request, 'Sucssesfull Create User')
                return redirect ('/')
        else:
            messages.info(request, 'PASSWORD NOT MUCH')
            return render(request,'Company/add-agent.html',{})
    return render(request,'Company/add-agent.html',{})


def show_profile(request):
    admin=Admin.objects.get(id=request.user.id)
    usermodel=admin.user
    context = {
        'admin':admin ,
        'usermodel':usermodel
    }

    return render(request,'Company/show_profile.html',context)

def edit_profile(request):
    admin=Admin.objects.get(id=request.user.id)
    usermodel=admin.user
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
        usermodel.first_name=request.POST['first_name']
        if len(request.FILES['img']) != 0:
            admin.profile_pic.delete()
            admin.profile_pic=request.FILES['img']
        admin.save()
        usermodel.save()
        return redirect ('show_profile')
    return render(request,'Company/edit_profile.html',context)



def change_password(request):
    admin=Admin.objects.get(id=request.user.id)
    u = User.objects.get(username__exact=request.user.username)
    
    
    context = {
        'admin':admin ,
       }
    if request.method == 'POST':
        if request.POST.get("change"):
            oldpassword=request.POST['oldpassword']
            newpassword=request.POST['newpassword']
            u.set_password(newpassword)
            u.save()

    return render(request,'Company/chage_password.html',context)


def change_password_m(request):
    user=User.objects.get(id=request.user.id)
  
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            usermodel = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Company/chage_password.html', {
        'form': form
    })

def change_profile_pic(request):
    admin=Admin.objects.get(id=request.user.id)
    usermodel=admin.user
    context = {
        'admin':admin ,
        'usermodel':usermodel
    }
    if request.method == 'POST':
        if len(request.FILES['img']) != 0:
            admin.profile_pic.delete()
            admin.profile_pic=request.FILES['img']
            admin.save()
            return redirect ('edit_profile')
        else:
            return render(request,'Company/change_profile_pic.html',context)
    return render(request,'Company/change_profile_pic.html',context)

def delete_profile_pic(request):
    admin=Admin.objects.get(id=request.user.id)
    usermodel=admin.user
    context = {
        'admin':admin ,
        'usermodel':usermodel
    }
    if len(admin.profile_pic) != 0:
        admin.profile_pic.delete()
        return redirect ('edit_profile')
    
    return render(request,'Company/edit_profile.html',context)


def add_staff(request):
    return render(request,'Company/add-staff.html',{})

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

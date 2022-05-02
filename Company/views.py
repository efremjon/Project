from multiprocessing.dummy import JoinableQueue
from django.contrib import messages
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
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


def user_profile(request):
    admin=Admin.objects.get(id=request.user.id)
    usermodel=admin.user
    context = {
        'admin':admin
    }

    if request.method == 'POST':
        if request.POST.get("change"):
            oldpassword=request.POST['oldpassword']
            newpassword=request.POST['newpassword']
            usermodel.set_password(newpassword)
            usermodel.save()

        if request.POST.get("save"):
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
        return redirect ('users-profile')

    return render(request,'Company/users-profile.html',context)

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

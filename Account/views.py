from multiprocessing import context
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Company.models import *
from .form import CreateSuperUser
# Create your views here.
def login_view(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user.groups.exists():
            a=user.groups.all()[0].name
            if a == 'Admin':
                login(request,user)
                return redirect('admin-dashbord',)
            elif a == 'Agent':
                login(request,user)
                return redirect('agent_dashbord')
            elif a == 'Customer':
                login(request,user)
                return redirect('Customer_dashbord')
            elif a == 'Financ_admin':
                login(request,user)
                return redirect('finance_admin_home')
            elif a == 'Store_Manager':
                login(request,user)
                return redirect('store-manager-home')
        else:
            return render(request,'Account/login.html')
    return render(request,'Account/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
   
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        Full_Name = first_name + " " + last_name
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username taken')
                return render(request,'Account/pages-register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken ')
                return render(request,'Account/pages-register.html')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
                user.save()
                group = Group.objects.get(name='Admin')
                user.groups.add(group)
                Admin.objects.create(user=user)
                messages.info(request, 'Sucssesfull Create User')
                return redirect ('/')
        else:
            print('user is not crated')
            return render(request,'Account/pages-register.html')
    else:
       
        messages.info(request, 'password not match') 
      
    return render(request,'Account/pages-register.html',)

def SuperUser_CreateView(request):
    if request.method == 'POST':
        form = CreateSuperUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            Full_Name = first_name + " " + last_name
            user=User.objects.get(username=username)
            group = Group.objects.get(name='Admin')
            user.groups.add(group)
            Admin.objects.create(user=user,Full_Name=Full_Name)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CreateSuperUser()
    context={
        
        'form':form,
    }
    return render(request,'Account/register-form2.html',context)

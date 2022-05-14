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
from Agent.models import Agent_order
from .form import passwordform,NameForm
from django.core.mail import send_mail

# Create your views here.

def Admin_dashboard(request):
    all_agent = Agent.objects.all()
    S_staff = Company_Store_Manager.objects.all()
    F_staff = Finance_Manager.objects.all()
    total_agent = all_agent.count()
    tottal_staff = S_staff.count() + F_staff.count()
    all_store = Company_Store.objects.all()
    tottal_store = all_store.count()
    all_region = Region.objects.all()
    tottal_region = all_region.count()
    all_product = Product.objects.all()
    tottal_product = all_product.count()
    all_product_in_store=Product_Amount_in_Store.objects.all()
    names = []
    for name in all_product:
        names.append(name.Product_Name)
    
    context = {
        'all_agent' : all_agent,
        'total_agent' :total_agent,
        'tottal_staff' : tottal_staff,
        'tottal_store' : tottal_store,
        'tottal_region': tottal_region,
        'tottal_product' : tottal_product,
        'all_product_in_store' :all_product_in_store,
        'names' :names,
    }
    return render(request,'Company/admin.html',context)

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
                return render(request,'Company/agents/add-agent.html',{})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken ')
                return render(request,'Company/agents/add-agent.html',{})
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
            return render(request,'Company/agents/add-agent.html',{})
    return render(request,'Company/agents/add-agent.html',{'form':form})

# ////////////////

# Profile
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
# end profile

# //////////////

# Manage Staff 
def view_staff(request):
    staff_finance_manager = Finance_Manager.objects.all()
    staff_company_store_manager = Company_Store_Manager.objects.all()
    context = {
       'staff_finance_manager' :staff_finance_manager,
       'staff_company_store_manager':staff_company_store_manager,
    }
    return render(request,'Company/staffs/staff-view.html',context)


def staff_profile(request,pk,staff):
    if staff=='Finance_manager':
         staff_detail = Finance_Manager.objects.get(id=pk)
         context = {'staff_detail':staff_detail}
    elif staff=='Store_Manager':
        staff_detail= Company_Store_Manager.objects.get(id=pk)
        context = {'staff_detail':staff_detail}
    else:
        context = {}
    return render(request,'Company/staffs/staff-detail.html',context)


def add_staff(request):
    return render(request,'Company/staffs/add-staff.html',{})

def update_staff(request,pk,staff):
    if staff=='Finance_manager':
         staff_detail = Finance_Manager.objects.get(id=pk)
         
         context = {'staff_detail':staff_detail}
         if request.method == 'POST':
            #  staff_detail.staff=request.POST['job']
             staff_detail.salary=request.POST['salary']
             staff_detail.save()
             return redirect('view-staff')
            
    elif staff=='Store_Manager':
        staff_detail= Company_Store_Manager.objects.get(id=pk)
        context = {'staff_detail':staff_detail}
    else:
        context = {}
    

    return render(request,'Company/staffs/update_staff.html',context)

def remove_staff(request,pk,staff):
    if staff=='Finance_manager':
         staff_detail = Finance_Manager.objects.get(id=pk)
         context = {'staff_detail':staff_detail}
    elif staff=='Store_Manager':
        staff_detail= Company_Store_Manager.objects.get(id=pk)
        context = {'staff_detail':staff_detail}
    else:
        context = {}
    return render(request,'Company/staffs/remove_staff.html',context)
    

# end Staff



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

# agent management

def agent_view(request):
    all_agent = Agent.objects.all()
    context = {
        'all_agent':all_agent,
    }
    return render(request,'Company/agents/agent-view.html',context)

def agent_detail(request,pk):
    agent = Agent.objects.get(pk=pk)
   
    context = {
        'agent':agent,      
    }
    return render(request,'Company/agents/agent-detail.html',context)

def agent_update_contrat(request,pk):
    agent = Agent.objects.get(pk=pk)
    context = {
        'agent':agent,      
    }
    return render(request,'Company/agents/update_agent.html',context)

def remove_agent(request,pk):
    agent = Agent.objects.get(pk=pk)
    context = {
        'agent':agent,      
    }
    return render(request,'Company/agents/remove_agent.html',context)
# Manage Store 

def view_store(request):
    all_store = Company_Store.objects.all()
    context = {
        'all_store' : all_store,
    }
    return render(request,'Company/store/store-view.html',context)

def add_store_company(request):
    return render(request,'Company/store/add-store.html')

def sore_ditel_view(request):
    all_product = Product.objects.all()
    store = Company_Store.objects.get(id=5)
    amount_store = Product_Amount_in_Store.objects.get(store=store)
    Dopple = 'Dopple'
    context = {
        'all_product' : all_product,
        'store': store,
        'amount': amount_store,
        'a' : Dopple,
    }
    return render(request,'Company/storeditel.html',context)

# end Manage store

# Manage Region

def view_region(request):
    all_region = Region.objects.all()
    context = {
        'all_region' : all_region,
    }
    return render(request,'Company/region/region-view.html',context)

def add_region(request):
    return render(request,'Company/region/add-region.html')

# end Region

def advertisments_view(request):
    return render(request,'Company/advertisments/advertisments.html')



def product_in_store(request):
    all_Product_Amount_in_Store = Product_Amount_in_Store.objects.all()
    # p_a=Product_Amount_in_Store.objects.get(Store=1,Product_Name=2)
    all_Product = Product.objects.all()
    all_Company_Store = Company_Store.objects.all()
    

    #  Name, id, produc_store, product_Quintitiy
 
#  store manager

def store_manager_view(request):
    user = User.objects.get(id=request.user.id)
    # a=Company_Store_Manager.objects.get(user=user)
   
    context = {
       'user' : user,
    #    'a' :a,
      
        
    }
    return render(request,'Company/store_manager/home_page.html',context)
def add_produc_to_store_view(request):
    return render(request,'Company/store_manager/add_to_store.html',{})

def aprove_order_view(request):
    return render(request,'Company/store_manager/approved_orders.html',{})

# END store manager



#  Finance admin

def finance_admin_view(request):
    return render(request,'Company/finance/home_page.html',)
def check_store_view(request):
    return render(request,'Company/finance/check-store.html',{})

def aprove_order_history_view(request):
    return render(request,'Company/finance/approved-orders-history.html',{})

# END store manager
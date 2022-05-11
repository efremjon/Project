from django.urls import path
from .import views
urlpatterns = [
   
    path('',views.Agent_dashboard,name="agent_dashbord"),

#   profile part

    path('show_profile/',views.show_profile,name='show_profile_agent'),
    path('edit_profile/',views.edit_profile,name='edit_profile_agent'),
    path('change_password/',views.change_password,name='change_password_agent'),
    path('change_profile_pic/',views.change_profile_pic,name='change_profile_pic_agent'),
    path('delete_profile_pic/',views.delete_profile_pic,name='delete_profile_pic_agent'),



    path('cusomer_order/',views.customer_order,name="customer_order"),
    path('agent_make_order/',views.make_order,name="agent_make_order"),
    path('manage_customers/',views.manage_customers,name="manage_customers"),
    path('manage_drivers/',views.manage_drivers,name="manage_drivers"),
    path('transactions/',views.transactions,name="transactions"),
    path('send_message/',views.send_message,name="send_message"),

]

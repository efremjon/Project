from django.urls import path
from .import views
urlpatterns = [
   
    path('',views.Agent_dashboard,name="agent_dashbord"),
    path('cusomer_order/',views.customer_order,name="customer_order"),
    path('make_order/',views.make_order,name="make_order"),
    path('manage_customers/',views.manage_customers,name="manage_customers"),
    path('manage_drivers/',views.manage_drivers,name="manage_drivers"),
    path('transactions/',views.transactions,name="transactions"),
    path('send_message/',views.send_message,name="send_message"),

]

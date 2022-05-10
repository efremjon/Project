from django.urls import path
from .import views
urlpatterns = [
    path('',views.Customer_dashboard,name="Customer_dashbord"),

    path('show_profile/',views.show_profile,name='show_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),


    path('make_order/',views.make_order,name="make_order"),
    path('send_delivery/',views.send_delivery,name="send_delivery"),
    path('transaction_history/',views.transaction_history,name="transaction_history"),
        
]

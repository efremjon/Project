from django.urls import path
from .import views
urlpatterns = [
    path('',views.Customer_dashboard,name="Customer_dashbord"),
    
    
    
]

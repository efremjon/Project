from django.urls import path
from .import views
urlpatterns = [
    path('',views.Agent_dashboard,name="agent_dashbord"),
    
    
]

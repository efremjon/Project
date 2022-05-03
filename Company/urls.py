from django.urls import path
from .import views
urlpatterns = [
    path('',views.Admin_dashboard,name="admin-dashbord"),
    path('add-agent/',views.add_agent,name='add-agent'),

    
    path('show_profile/',views.show_profile,name='show_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('change_profile_pic/',views.change_profile_pic,name='change_profile_pic'),
    path('delete_profile_pic/',views.delete_profile_pic,name='delete_profile_pic'),


    path('add-staff/',views.add_staff,name='add-staff'),
    path('remove-staff/',views.remove_staff,name='remove-staff'),
    path('view-agent-orders/',views.view_agent_orders,name='view-agent-orders'),
    path('approve-agent-orders/',views.approve_agent_orders,name='approve-agent-orders'),
    path('store/',views.store,name='store'),
    path('contact-store-manager/',views.contact_store_manager,name='contact-store-manager'),
    path('agent-report/',views.agent_report,name='agent-report'),
    path('finance-report/',views.finance_report,name='finance-report'),
    path('advertisements/',views.advertisements,name='advertisements'),
     path('remove-agent/',views.remove_agent,name='remove-agent'),
     path('agent-view/',views.agent_view,name='agent-view'),
     path('agent-detail/',views.agent_detail,name='agent-detail'),

]

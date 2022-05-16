from django.urls import path
from .import views
urlpatterns = [
    path('',views.Admin_dashboard,name="admin-dashbord"),
   
   path('agent_dashboard',views.staff_dashboard,name="dashbord-staff"),
   path('store_dashboard',views.store_dashboard,name="dashbord-store"),
   path('region_dashboard',views.region_dashboard,name="dashbord-region"),
   path('product_dashboard',views.product_dashboard,name="dashbord-product"),

    
    path('show_profile/',views.show_profile,name='show_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('change_profile_pic/',views.change_profile_pic,name='change_profile_pic'),
    path('delete_profile_pic/',views.delete_profile_pic,name='delete_profile_pic'),

# Agent Management Part
    path('add-agent/',views.add_agent,name='add-agent'),
    path('agent-view/',views.agent_view,name='agent-view'),
    path('agent-detail/<int:pk>',views.agent_detail,name='agent-detail'),
    path('update_contrat/<int:pk>',views.agent_update_contrat,name='update_contrat'),
    path('remove-agent/<int:pk>',views.remove_agent,name='remove-agent'),
    path('agent-report/',views.agent_report,name='agent-report'),
    path('view-agent-orders/',views.view_agent_orders,name='view-agent-orders'),
    path('approve-agent-orders/',views.approve_agent_orders,name='approve-agent-orders'),
# end Agent Management Part 

# ////////////////////////

# Manage Stafe

    path('view-staff/',views.view_staff,name='view-staff'),
    path('add-staff/',views.add_staff,name='add-staff'),
    path('staff-detail/<int:pk>/<str:staff>',views.staff_profile,name='staff-detail'),
    path('update-staff/<int:pk>/<str:staff>',views.update_staff,name='update-staff'),
    path('remove-staff/<int:pk>/<str:staff>',views.remove_staff,name='remove-staff'),

# end manage staff 
    path('approve-agent-orders/',views.approve_agent_orders,name='approve-agent-orders'),
    path('store/',views.store,name='store'),
    path('contact-store-manager/',views.contact_store_manager,name='contact-store-manager'),
    path('finance-report/',views.finance_report,name='finance-report'),
    path('advertisements/',views.advertisements,name='advertisements'),
    
     
# Manage store part

    path('view_store/',views.view_store,name='view-store'),
    path('add_store_company/',views.add_store_company,name='add-store-company'),
    path('store_detile/<int:pk>',views.sore_ditel_view,name="store_detile"),
# end Manage store part

# Manage region part

    path('view_region/',views.view_region,name='view-region'),
    path('add_region/',views.add_region,name='add-region'),

# endregion part

# Manage Product

path('view_product/',views.view_product,name='view-product'),
path('add_product/',views.add_product,name='add-product'),
path('update_product/<int:pk>',views.update_product,name='update-product'),

# End Product

path('add_advertisments/',views.advertisments_view,name='add-advertisments'),

# END Addivertisment


# Report 
 path('view_report/',views.view_report,name='view-report'),

# END Report

# store manager 

path('Store_Manager/',views.store_manager_view,name='store-manager-home'),
path('Store_Manager/add_produc_to_store',views.add_produc_to_store_view,name='add-to-store'),
path('Store_Manager/aprove_order',views.aprove_order_view,name='aprove-order'),
# endstore manager

# finance admin
path('Finance_Admin/',views.finance_admin_view,name='finance_admin_home'),
path('Finance_Admin/check_store',views.check_store_view,name='finance-check-store'),
path('Finance_Admin/aprove_order_history',views.aprove_order_history_view,name='aprove-order-history'),

# end finace admin
]

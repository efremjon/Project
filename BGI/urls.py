
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Account.urls')),
    path('BGI/',include('Company.urls')),
    path('Agent/',include('Agent.urls')),
    path('Customer/',include('Customer.urls')),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

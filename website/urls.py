from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Core import views

urlpatterns = [
    path('', include('Core.urls')),
    path('quotes/<str:pk>', include('Price.urls')),    
    path('admin/', admin.site.urls),
]

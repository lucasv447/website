from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Price import views

urlpatterns = [
    path('', views.quotes, name='quotes'),
    

]
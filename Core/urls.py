from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.entrar, name='entrar'),

]

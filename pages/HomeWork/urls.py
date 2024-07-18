from django.urls import path

from . import views

app_name = "HW"

urlpatterns = [
    path('', views.HomeWork, name ='ind') 
    ]
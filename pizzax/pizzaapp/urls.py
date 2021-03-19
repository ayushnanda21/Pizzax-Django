from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .import views

urlpatterns = [
    path('admin/',views.adminLoginview, name="adminLoginpage"),
    path('adminauthenticate/' ,views.authenticateadmin, name="authenticateadmin"),
    path('admin/homepage/',views.adminhomepageview, name="adminhomepage"),
    path('adminlogout/', views.logoutadmin, name="logoutadmin")
    
]

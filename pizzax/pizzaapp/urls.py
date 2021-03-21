from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .import views

urlpatterns = [
    path('admin/',views.adminLoginview, name="adminLoginpage"),
    path('adminauthenticate/' ,views.authenticateadmin, name="authenticateadmin"),
    path('adminhomepage/',views.adminhomepageview, name="adminhomepage"),
    path('adminlogout/', views.logoutadmin, name="logoutadmin"),
    path('addpizza/',views.addpizza , name="addpizza"),
    path('deletepizza/<int:pizzapk>/',views.deletepizza, name="deletepizza"),
    path("", views.homepageview, name="homepageview"),
    path("signupuser/", views.signupuser ,name="signupuser"),
    
]

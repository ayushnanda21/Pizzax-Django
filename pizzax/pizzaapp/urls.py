from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .import views

urlpatterns = [
    path('adminuser/',views.adminLoginview, name="adminLoginpage"),
    path('adminauthenticate/' ,views.authenticateadmin, name="authenticateadmin"),
    path('adminhomepage/',views.adminhomepageview, name="adminhomepage"),
    path('adminlogout/', views.logoutadmin, name="logoutadmin"),
    path('addpizza/',views.addpizza , name="addpizza"),
    path('deletepizza/<int:pizzapk>/',views.deletepizza, name="deletepizza"),
    path("", views.homepageview, name="homepageview"),
    path("signupuser/", views.signupuser ,name="signupuser"),
    path("loginuser/", views.userloginview , name="userloginpage"),
    path("customer/welcome", views.customerwelcomeview ,name="customerpage"),
    path("customer/authenticate/" ,views.userauthenticate   ,name="userauthenticate"),
    path("userlogout/" ,views.userlogout ,name="userlogout"),
    path("placeorder/", views.placeorder, name="placeorder"),
    path("userorders/", views.userorders, name="userorders")    
]

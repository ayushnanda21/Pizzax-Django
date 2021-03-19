from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

def adminLoginview(request):
    return render(request,"pizzaapp/adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user=   authenticate(username = username, password = password)
    if user is not None and user.username=="admin":
        login(request,user)
        return redirect('adminhomepage')
      
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Crediantials")
        return redirect('adminLoginpage')


def adminhomepageview(request):
    return render(request,"pizzaapp/adminhomepage.html" )
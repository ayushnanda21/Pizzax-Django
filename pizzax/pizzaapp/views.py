from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PizzaModel, CustomerModel
from django.contrib.auth.models import User

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
    context={'pizzas' : PizzaModel.objects.all()}
    return render(request,"pizzaapp/adminhomepage.html",context )


def logoutadmin(request):
    logout(request)
    return redirect('adminLoginpage')

def addpizza(request):
    name= request.POST['pizza']
    price= request.POST['price']
    PizzaModel(name= name, price = price).save()    #to add pizza to db
    return redirect('adminhomepage')

def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')

#for customer displays

def homepageview(request):
    return render(request,"pizzaapp/homepage.html")

def signupuser(request):
    username = request.POST['username']
    password= request.POST['password']
    phonenumber=request.POST['phonenumber']

    #if username already exists
    if User.objects.filter(username =username).exists():
        messages.add_message(request, messages.ERROR, "Username already exists")
        return redirect('homepageview')

    #if username does'nt exist (everything is fine)
    
    User.objects.create_user(username =username, password =password).save()
    lastobject = len(User.objects.all()) - 1
    CustomerModel(userid =User.objects.all()[int(lastobject)].id, phonenumber =phonenumber).save()
    messages.add_message(request, messages.ERROR, "Account Created Successfully")
    return redirect('homepageview')

#views and login for user

def userloginview(request):
    return render(request,"pizzaapp/userlogin.html")

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user=   authenticate(username = username, password = password)
    if user is not None:
        login(request,user)
        return redirect('customerpage')
      
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Crediantials")
        return redirect('userloginpage')

def customerwelcomeview(request):
    username=request.user.username
    context ={"username" : username}
    return render(request,"pizzaapp/customerwelcome.html",context)

def userlogout(request):
    logout(request)
    return redirect('userloginpage')

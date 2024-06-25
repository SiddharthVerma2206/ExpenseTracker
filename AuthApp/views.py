from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages

# Create your views here.
def signup(request):
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():     
            messages.error(request , "User Already Exists. Try Logging In")
            return redirect('homePage')
        else:
            user= User.objects.create_user(username=username ,email=email  , password=password)
            user.save()
            login(request , user)
            return redirect('homePage')
            
        
def login_user(request):
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user= authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('homePage')
        else:
            messages.error(request , "Username Or Password Is Incorrect!")
            return redirect('homePage')
        
def logout_user(request):
    logout(request)
    return redirect('homePage')
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
            return redirect('Landing')
        else:
            user= User.objects.create_user(username=username ,email=email  , password=password)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('homePage')
            
        
def login_user(request):
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user= authenticate(request , username=username , password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('homePage')
        else:
            messages.error(request , "Username Or Password Is Incorrect!")
            return redirect('Landing')
        
def logout_user(request):
    logout(request)
    return redirect('Landing')

def delete_user(request): 
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('Landing')
         
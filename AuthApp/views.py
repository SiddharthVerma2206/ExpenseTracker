from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        user= User.objects.create_user(request.POST['username'] , password=request.POST['password'] , email=request.POST['email'])
        user.save()
        login(request , user)
        return redirect('homePage')
        
def login_user(request):
    if request.method=="GET":
        return render(request , 'login.html')
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user= authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('homePage')
        else:
            return render(request , "login.html" , {})
        
def logout_user(request):
    logout(request)
    return redirect('homePage')
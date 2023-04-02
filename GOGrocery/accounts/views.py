from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username', "default value")
        password1 = request.POST.get('password1', "default value")
        password2 = request.POST.get('password2', "default value")
        email = request.POST.get('email', "default value")
        print("email")

       
        
        return redirect('home')
    else:
        return render(request,'register.html')
    
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User = authenticate(request, username=username, password=password)

        if User is not None:
            login(request, User)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
           
    context = {}
    return render(request, 'login', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



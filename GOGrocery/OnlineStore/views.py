

# Create your views here.
from django.shortcuts import render, redirect
from .models import Store
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    return render (request, "home.html")

def groceryList(request):
    return render (request, "groceryList.html")
    

def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        
        return redirect('login')
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


def groceryList(request):
    return render (request, "groceryList.html")

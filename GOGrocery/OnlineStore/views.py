

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
from .models import Store
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render (request, "home.html")

def groceryList(request):
    return render (request, "groceryList.html")

def groceryItems(request):
    return render (request, "groceryItems.html")
    

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



def my_lists(request):
     if request.method == "GET":
        shopping_lists = Store.objects.filter(user=request.user)
        return render(request, "groceryList.html", context = {"shopping_lists":shopping_lists})

     if request.method == "POST":
        if request.POST.get('reciepe_add'):
            print(request.POST)
            checked = False
            if request.POST.get('checkbox'):
                checked = True
            item_name = request.POST.get("reciepe")
            Store.objects.create(title = item_name, user=request.user, is_public = checked)
     
         
        elif request.POST.get('delete'):
               id_to_delete = request.POST.get("delete")
               item_to_delete = Store.objects.get(
                   pk=id_to_delete)
               item_to_delete.delete()
               
        return redirect('home') 




    


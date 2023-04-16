# Create your views here.
from django.shortcuts import render, redirect
from .models import Store, GroceryItems
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
    items = GroceryItems.objects.all()
    if request.method == 'POST':
        if request.POST.get('item_add'):
            veg_name = request.POST['vegetable_name']
            quantity = request.POST['quantity']
            GroceryItems.objects.create(name=veg_name, quantity= int(quantity))
        elif request.POST.get('delete'):
               id_to_delete = request.POST.get("delete")
               item_to_delete = GroceryItems.objects.get(
                   pk=id_to_delete)
               item_to_delete.delete()
        elif request.POST.get('checkbox'):
            ids_to_update = request.POST.getlist("checkbox")
            print(ids_to_update)
            for item in items:
                item_to_update = GroceryItems.objects.get(
                    pk=item.pk)
                item_to_update.is_organic= str(item.pk) in ids_to_update
                print(item.pk, ids_to_update, item_to_update.is_organic)
                item_to_update.save()
                items = GroceryItems.objects.all()
        else:
            for item in items:
                item_to_update = GroceryItems.objects.get(
                    pk=item.pk)
                item_to_update.is_organic= False
                item_to_update.save()
                items = GroceryItems.objects.all()

        return render (request, "groceryItems.html", context={'items':items})
    
    return render (request, "groceryItems.html", context={'items':items})
    

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
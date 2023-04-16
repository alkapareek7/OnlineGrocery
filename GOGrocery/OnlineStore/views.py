

# Create your views here.
from django.shortcuts import render, redirect
<<<<<<< HEAD
from .models import Store, GroceryItems
=======
from .models import GroceryList, RecipeList
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9
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
<<<<<<< HEAD
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
=======

    if request.method == "GET":
        grocery_lists = GroceryList.objects.filter(user=request.user)
        return render(request, "groceryList.html", context={"grocery_lists": grocery_lists})
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9
    
    if request.method == "POST":
        if request.POST.get("recipe_add"):
            checked = False
            if request.POST.get("checkbox"):
                checked = True

            item_name = request.POST.get("recipe") 
            GroceryList.objects.create(title = item_name, user = request.user, is_public=checked)
        elif request.POST.get("delete"):
            id_to_delete = request.POST.get("delete")
            item_to_delete = GroceryList.objects.get(pk=id_to_delete)
            item_to_delete.delete()
        return redirect("lists-list")
    

def reciepeLists(request, pk):
    shopping_list = RecipeList.objects.get(pk=pk)
    items_list = shopping_list.shoppingitem_set.all()

    if request.method == "GET":
        return render(request, "reciepeLists.html", context={"shopping_list": items_list, "header" : shopping_list})
    
    if request.method == "POST":
        if request.POST.get("item_add"):
            item_name = request.POST.get("item_name")
            item_description = request.POST.get("item_description")

            shopping_list.shoppingitem_set.create(name=item_name, description=item_description)

        elif request.POST.get("update_checked"):
            checked = request.POST.getlist("checkbox")
            for item in items_list:
                item.is_completed = True if str(item.pk) in checked else False
                item.save()
        elif request.POST.get("delete"):
            id_to_delete = request.POST.get("delete")
            item_to_delete = shopping_list.shoppingitem_set.get(pk=id_to_delete)
            item_to_delete.delete()

        return redirect("items-list", pk)
        

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
<<<<<<< HEAD



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




    

=======
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9

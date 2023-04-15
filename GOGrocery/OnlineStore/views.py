

# Create your views here.
from django.shortcuts import render, redirect
from .models import GroceryList, RecipeList
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

    if request.method == "GET":
        grocery_lists = GroceryList.objects.filter(user=request.user)
        return render(request, "groceryList.html", context={"grocery_lists": grocery_lists})
    
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

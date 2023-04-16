from django.urls import include, path
from . import views
from .views import groceryList, home
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls import path, include
from .views import registerPage, loginPage , home, groceryList, groceryItems
from django.contrib.auth.decorators import login_required





urlpatterns = [
    path('', views.home, name='home'),
    path("registerPage/", login_required(registerPage), name="registerPage"),
    path("loginPage/", login_required(loginPage), name= "loginPage"),
    path("groceryList/", groceryList, name= "groceryList"),
    path("groceryItems/", groceryItems, name= "groceryItems"),
    
]
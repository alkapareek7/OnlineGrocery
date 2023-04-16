from django.urls import include, path
from . import views
from .views import groceryList, home
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls import path, include
<<<<<<< HEAD
from .views import registerPage, loginPage , home, groceryList, groceryItems
=======
from .views import registerPage, loginPage , home, groceryList, reciepeLists
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9
from django.contrib.auth.decorators import login_required





urlpatterns = [
    path('', views.home, name='home'),
    path("registerPage/", login_required(registerPage), name="registerPage"),
    path("loginPage/", login_required(loginPage), name= "loginPage"),
    path("groceryList/", groceryList, name= "groceryList"),
<<<<<<< HEAD
    path("groceryItems/", groceryItems, name= "groceryItems"),
    
=======
    path("reciepeLists/", reciepeLists, name= "reciepeLists"),
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9
]
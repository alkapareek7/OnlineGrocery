from django.urls import path, include
from .views import registerPage,loginPage

urlpatterns = [

    path("", include("django.contrib.auth.urls")),
    path("register/", registerPage, name="registerPage"), 
    path("login/", loginPage, name="loginPage"),

]


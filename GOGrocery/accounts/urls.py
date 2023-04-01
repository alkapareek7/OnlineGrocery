from django.urls import path, include
from .views import registerPage

urlpatterns = [

    path("", include("django.contrib.auth.urls")),
    path("register/", registerPage, name="registerPage"), 

]


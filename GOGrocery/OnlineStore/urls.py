from django.urls import include, path
from . import views
from .views import home
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path





urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),    
    path('logout/', LogoutView.as_view(), name='logout'),

    ]

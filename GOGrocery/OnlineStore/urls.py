from django.urls import include, path
from . import views
from .views import home


urlpatterns = [
    path('', views.home, name='home'),

]

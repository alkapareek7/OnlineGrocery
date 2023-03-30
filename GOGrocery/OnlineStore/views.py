from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Store
# Create your views here.
def home(request):
    return render (request, "home.html")
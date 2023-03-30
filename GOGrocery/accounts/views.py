from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.object.create_user(username=username, password=password1, email=email)
        user.save();
        print('User created')
        return redirect('/')
    else:
        return render(request,'register.html')
    
def login(request):
    return render(request, 'login.html')
from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Store
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView



from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def home(request):
    return render (request, "home.html")


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    



class MyLogOutView(TemplateView):
    template_name = "registration/logged_out.html"
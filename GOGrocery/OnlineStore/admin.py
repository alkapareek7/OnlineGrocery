from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from .models import Store, groceryList

# Register your models here.

admin.site.register(Store)
admin.site.register(groceryList)
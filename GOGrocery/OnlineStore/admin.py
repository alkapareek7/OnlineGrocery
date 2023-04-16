from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from .models import Store, groceryList, GroceryItems
# Register your models here.

admin.site.register(Store)
admin.site.register(groceryList)
admin.site.register(GroceryItems)


from django.apps import AppConfig


class OnlinestoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "OnlineStore"

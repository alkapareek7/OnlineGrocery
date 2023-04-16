from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
from django.db.models import (
CASCADE, CharField, ForeignKey, Model, BooleanField, DateField, IntegerField)
from datetime import datetime

from django.urls import reverse

# Create your models here.

class ItemsAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id']
    list_display = ['id', 'name','grocery_list', 'description', 'is_completed']
    list_display_links = ['id', 'name','description']
    list_per_page = 30
    list_filter = ['description']
    search_fields = ['name']
    actions = ['cleanup_description']
    fieldsets = [
        (None, {'fields': ['name']}),
        (
            'Link to Another table',
            {
                'fields': ['grocery_list'],
                'description': (
                    'Select form the list of possible lists.'
                )
            }
        ),
        (
            'Item Information',
            {
                'fields': ['description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['is_completed']


class Store(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(max_length=20)

class GroceryList(Model):
    Vegetable_name = CharField('Shopping list item name', max_length=100)
    user = ForeignKey(User, on_delete = CASCADE)
    created_at = DateField(default=datetime.now())
    is_organic = BooleanField(default=False)
    quantity = IntegerField(max_length=100)

<<<<<<< HEAD
class GroceryItems(Model):
    name = CharField('Shopping list name', max_length=100)
    is_organic = BooleanField(default=False)
    quantity = IntegerField(max_length=100)


class ItemsAdmin(ModelAdmin):

    
    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id']
    list_display = ['id', 'name', 'shopping_list','description', 'is_completed']
    list_display_links = ['id', 'name']
    list_per_page = 3
    list_filter = ['description']
    search_fields = ['name']
    actions = ['cleanup_description']
    fieldsets = [
        (None, {'fields': ['name']}),
        (
        'Link another table',
        {
            'fields': ['shopping_list'],
            'description': (
                'Select from the list of possible lists'
                
            )
        }
        ),
        (
        'User Information',
        {
            'fields': ['description'],
            'description': 'These fields are intended to be filled in by our users.'
        }
        )
  ]
readonly_fields = ['is_completed']
=======
    def __str__(self):
        return self.title

class RecipeList(Model):
    name= CharField("Grocery list item name", max_length=100)
    description = CharField("Shopping list item description", max_length=300, null=True, blank=True)
    is_completed = BooleanField(default=False)
    grocery_list = ForeignKey(GroceryList, on_delete=CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items-list', kwargs={'pk': self.grocery_list.pk})

>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9

from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
from django.db.models import (
CASCADE, CharField, ForeignKey, Model, BooleanField, DateField, IntegerField)
from datetime import datetime

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(max_length=20)

class groceryList(Model):
    Vegetable_name = CharField('Shopping list name', max_length=100)
    user = ForeignKey(User, on_delete = CASCADE)
    created_at = DateField(default=datetime.now())
    is_organic = BooleanField(default=False)
    quantity = IntegerField(max_length=100)
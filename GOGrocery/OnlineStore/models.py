from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.decorators import login_required

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default= False)

@login_required
def my_view(request):
    pass
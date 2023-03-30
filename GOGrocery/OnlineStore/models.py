from django.db import models
<<<<<<< HEAD

# Create your models here.
from django.db import models
from django.contrib.auth.decorators import login_required
=======
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
>>>>>>> 6b226320b9ebc0ce4571eeb002b84e61a7f259ba

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default= False)

<<<<<<< HEAD
@login_required
def my_view(request):
    pass
=======
>>>>>>> 6b226320b9ebc0ce4571eeb002b84e61a7f259ba

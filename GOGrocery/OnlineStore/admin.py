from django.contrib import admin

# Register your models here.
from django.contrib import admin 
<<<<<<< HEAD
from .models import Store, groceryList, GroceryItems
# Register your models here.

admin.site.register(Store)
admin.site.register(groceryList)
admin.site.register(GroceryItems)
=======
from .models import Store, GroceryList

# Register your models here.

admin.site.register(Store)
admin.site.register(GroceryList)
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9

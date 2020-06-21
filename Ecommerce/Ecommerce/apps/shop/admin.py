from django.contrib import admin
from .models import ShopUser, Product, Cart

# Register your models here.

admin.site.register(ShopUser)
admin.site.register(Product) 
admin.site.register(Cart) 

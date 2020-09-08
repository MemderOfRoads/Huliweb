from django.contrib import admin

# Register your models here.
from .models import Item, OrderItem, Order, User

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(User)


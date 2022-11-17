from django.contrib import admin
from .models import Order, OrderItem, WatchItem, UserMember, Invoice

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(WatchItem)
admin.site.register(UserMember)
admin.site.register(Invoice)


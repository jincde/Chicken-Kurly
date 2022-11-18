from django.contrib import admin
from .models import OrderItem, WatchItem, User

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(WatchItem)
admin.site.register(User)



from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Ddib)
admin.site.register(DdibItem)
admin.site.register(Inquiry)
admin.site.register(Reply)
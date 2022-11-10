from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    sold_count = models.IntegerField(default=0)  # 상품 팔린 갯수
    buy_count = models.IntegerField(default=0)   # 구입할 상품 갯수
    hit = models.IntegerField(default=0)
    brand = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    cart_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='cart_products')
    ddib_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='ddib_products')


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
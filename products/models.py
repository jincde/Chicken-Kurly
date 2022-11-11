from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    sold_count = models.IntegerField(default=0)  # 상품 팔린 갯수
    quantity = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])   # 구입할 상품 갯수
    hit = models.IntegerField(default=0)
    brand = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')

# User - Cart (1:1)
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
    ])   # 구입할 상품 갯수
    
# User - Ddib (1:1)
class Ddib(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class DdibItem(models.Model):
    ddib = models.ForeignKey(Ddib, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# 상품 문의
class Inquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def status(self):
        return self._meta.model.status

# 문의 답변
class Reply(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE)
    # title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# 상품 후기
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=50)
    content = models.TextField('후기작성')
    created_at = models.DateTimeField(auto_now_add=True)

# 상품 후기 이미지
class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    review_img = models.ImageField('사진등록', upload_to='img/')
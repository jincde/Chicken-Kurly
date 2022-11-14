from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings
from products.models import Product


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[Thumbnail(60, 60)],
        format="JPEG",
        options={"quality": 90},
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_pk", editable=True,
    )
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )


class Order(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  created = models.DateTimeField(auto_now_add=True)
  paid = models.BooleanField(default=False)

  class Meta:
    ordering = ['-created']

  def __str__(self):
    return 'Order {}'.format(self.id)

  def get_total_product(self):
    return sum(item.get_item_price() for item in self.items.all())

  def get_total_price(self):
    total_product = self.get_total_product()
    return total_product - self.discount


class OrderItem(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
  ordered = models.BooleanField(default=False)
  order_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '{}'.format(self.id)
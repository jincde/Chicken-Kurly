from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings
from products.models import Product, DdibItem
from products.models import Product, Ddib
from django.core.validators import MinLengthValidator



# Create your models here.
class User(AbstractUser):
    BRONZE, SILVER, GOLD = "Bronze", "Silver", "Gold"
    
    rating_choices = (
        (BRONZE, "Bronze"),
        (SILVER, "Silver"),
        (GOLD, "Gold"),
    )

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
    address = models.CharField(max_length=50)
    username = models.CharField(validators=[MinLengthValidator(5)], max_length=16, unique=True)
    name = models.CharField(max_length=200, null=True)
    current_rating = models.IntegerField(default=500, verbose_name="Current Rating")
    rating = models.CharField(max_length=255, choices=rating_choices, default=BRONZE, verbose_name="rating")
    xp = models.IntegerField(default=10, verbose_name="XP")


    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"

    RATING_THRESHOLDS = {
        BRONZE: 10000,
        SILVER: 30000,
        GOLD: 50000,
    }
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
        

    def get_current_choice(self):
        rating = self.current_rating
        if rating < self.RATING_THRESHOLDS[self.BRONZE]:
            return self.BRONZE
        elif rating < self.RATING_THRESHOLDS[self.SILVER]:
            return self.SILVER
        elif rating < self.RATING_THRESHOLDS[self.GOLD]:
            return self.GOLD
        

    PARTICIPATION_XP, VIP_XP, V_VIP_XP = 10000, 30000, 50000

    def get_current_level_and_xp_threshold(self):
        current_xp = self.xp
        xp_threshold = 10000
        level = 1
        while current_xp > xp_threshold:
            level += 1
            xp_threshold += xp_threshold
        return level, xp_threshold


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


class OrderItem(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
  quantity = models.IntegerField()
  price = models.IntegerField()
  order_date = models.DateTimeField(auto_now_add=True)
  imp_uid = models.CharField(max_length=50)
  merchant_uid = models.CharField(max_length=50)
  
  def __str__(self):
    return '{}'.format(self.id)

  def get_item_price(self):
    return self.product.price * self.quantity


# ?????? ??????
class WatchItem(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ddib = models.ForeignKey(Ddib, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)



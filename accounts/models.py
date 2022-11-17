from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings
from products.models import Product, DdibItem
from products.models import Product, Ddib
from django.views.generic.dates import timezone_today
from collections import defaultdict




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
    address = models.CharField(max_length=50)
    username = models.CharField(min_lenghth=5, max_length=50, unique=True)

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
  quantity = models.IntegerField()
  ordered = models.BooleanField(default=False)
  order_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '{}'.format(self.id)

  def get_item_price(self):
    return self.price * self.quantity

# 찜한 상품
class WatchItem(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ddib = models.ForeignKey(Ddib, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)



# 등급
BRONZE_MEMBERSHIP = 1
SILVER_MEMBERSHIP = 2
GOLD_MEMBERSHIP = 3


MEMBERSHIP_AMOUNTS = {
    'gold': 50000,
    'silver': 30000,
    'bronze': 0,
}

MEMBERSHIP_LEVELS = (
    (BRONZE_MEMBERSHIP, 'Bronze'),
    (SILVER_MEMBERSHIP, 'Silver'),
    (GOLD_MEMBERSHIP, 'Gold'),
)

MEMBERSHIP_TO_KEY = dict((k, v.lower()) for k, v in MEMBERSHIP_LEVELS)

class UserMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=250)
    billing_name = models.CharField(
        max_length=250,
        blank=True,
        help_text='If different from display name.',
    )
    contact_name = models.CharField(max_length=250)
    contact_email = models.EmailField()
    billing_email = models.EmailField(blank=True, help_text='If different from contact email.',)
    membership_level = models.IntegerField(choices=MEMBERSHIP_LEVELS)
    address = models.TextField(blank=True)
    django_usage = models.TextField(blank=True, help_text='Not displayed publicly.')
    inactive = models.BooleanField(default=False, help_text='No longer renewing.')

    def for_public_display(self):
        objs = self.get_queryset().filter(
            invoice__expiration_date__gte=timezone_today(),
        ).annotate(purchased_amount=models.Sum('invoice__amount'))
        return objs.order_by('-purchased_amount', 'display_name')

    def by_membership_level(self):
        members_by_type = defaultdict(list)
        members = self.for_public_display()
        for member in members:
            key = MEMBERSHIP_TO_KEY[member.membership_level]
            members_by_type[key].append(member)
        return members_by_type
    
    def _is_invoiced(self):
        invoices = self.invoice_set.all()
        return bool(invoices) and all(invoice.sent_date is not None for invoice in invoices)
    _is_invoiced.boolean = True
    is_invoiced = property(_is_invoiced)

    def _is_paid(self):
        invoices = self.invoice_set.all()
        return bool(invoices) and all(invoice.paid_date is not None for invoice in invoices)
    _is_paid.boolean = True
    is_paid = property(_is_paid)

    def get_expiry_date(self):
        expiry_date = None
        for invoice in self.invoice_set.all():
            if expiry_date is None:
                expiry_date = invoice.expiration_date
            elif invoice.expiration_date and invoice.expiration_date > expiry_date:
                expiry_date = invoice.expiration_date
        return expiry_date

class Invoice(models.Model):
    sent_date = models.DateField(blank=True, null=True)
    amount = models.IntegerField(help_text='In integer dollars')
    paid_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    member = models.ForeignKey(UserMember, on_delete=models.CASCADE)
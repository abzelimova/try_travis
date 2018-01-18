from django.db import models
import uuid
from django.contrib.auth.models import User

class Shop(models.Model):
    category = models.ForeignKey('Category', related_name="shop_category")
    


class Good(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='good_images')
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', related_name="good_category")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Order(models.Model):
#    customer = models.ForeignKey(User, related_name="order")
    address = models.CharField(max_length=150)
    datetime = models.DateField()
 #   goods = models.ForeignKey('UserBasketItems', related_name='order')


class UserBasketItems(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    good = models.ForeignKey('Good', related_name='goods_in_basket')
    count_of = models.IntegerField()

    def __str__(self):
        return self.uid


class Token(models.Model):
    token = models.CharField(max_length=140)

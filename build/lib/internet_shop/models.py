from django.db import models
import uuid


class Good(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='good_images')
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', related_name='goods')
    sizes = models.ManyToManyField('Sizes', related_name='good', blank=True)
    color = models.ManyToManyField('Colors', related_name='good', blank=True)

class Colors(models.Model):
    name = models.CharField(max_length=140)
    def __str__(self):
        return self.name

class Sizes(models.Model):
    name = models.CharField(max_length=140)
    def __str__(self):
        return  self.name

class Category(models.Model):
    name = models.CharField(max_length=140, unique=True)
    url_name = models.CharField(max_length=140, unique=True)
    parent = models.ForeignKey('self', blank=True, related_name='children', null=True)

    def __str__(self):
        return '-'*self.get_level() + ' ' +  self.name

    def get_level(self):
        parent = self.parent
        i = 0
        while parent is not None:
            parent = parent.parent
            i += 1

        return i


class UserBasketItems(models.Model):
  uid = models.UUIDField(default=uuid.uuid4, editable=False)
  good = models.ForeignKey('Good', related_name='goods_in_basket')
  count_of = models.IntegerField()
  color = models.ForeignKey('Colors', related_name="color_in_basket")
  size = models.ForeignKey('Sizes', related_name="size_in_basket")
from django.db import models
import uuid


class Good(models.Model):

    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='good_images')

    color = models.ForeignKey('Colors', related_name='good', blank=True, default=None, null=True)

    _sizes = (('XS', 'XS'), ('S', 'S') , ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'))
    size = models.CharField(max_length=140, choices=_sizes, blank=True)

    cost = models.DecimalField(max_digits=8, decimal_places=2)

    category = models.ForeignKey('Category', related_name='goods')


class Colors(models.Model):

    name = models.CharField(max_length=140)


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


class Basket(models.Model):

  uid = models.UUIDField(default=uuid.uuid4, editable=False)
  goods = models.ManyToManyField('Good', related_name='goods_in_basket')
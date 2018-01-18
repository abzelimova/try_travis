from django.contrib import admin

from internet_shop.models import Good, Category, Order, Shop

admin.site.register(Good)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Shop)

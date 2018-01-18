# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0004_remove_order_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_category', to='internet_shop.Category')),
            ],
        ),
    ]

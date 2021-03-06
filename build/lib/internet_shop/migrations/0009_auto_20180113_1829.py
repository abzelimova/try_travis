# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0008_auto_20180113_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.RemoveField(
            model_name='options',
            name='color',
        ),
        migrations.RemoveField(
            model_name='good',
            name='options',
        ),
        migrations.AddField(
            model_name='good',
            name='color',
            field=models.ManyToManyField(blank=True, related_name='good', to='internet_shop.Colors'),
        ),
        migrations.DeleteModel(
            name='Options',
        ),
        migrations.AddField(
            model_name='good',
            name='size',
            field=models.ManyToManyField(blank=True, related_name='good', to='internet_shop.Size'),
        ),
    ]

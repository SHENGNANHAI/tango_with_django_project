# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-07 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20190207_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]

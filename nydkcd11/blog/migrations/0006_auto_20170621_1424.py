# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-21 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image_main/'),
        ),
    ]

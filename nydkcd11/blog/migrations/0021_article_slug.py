# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20170713_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20170620_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='editor',
            field=models.CharField(default=django.utils.timezone.now, max_length=75),
            preserve_default=False,
        ),
    ]

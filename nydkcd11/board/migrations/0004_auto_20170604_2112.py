# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20170514_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='desc',
            field=models.CharField(max_length=3000),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20170901_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

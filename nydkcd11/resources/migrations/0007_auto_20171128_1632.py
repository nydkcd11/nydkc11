# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_minutes_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutes',
            name='location',
            field=models.CharField(default='Division 11', max_length=50),
        ),
        migrations.AlterField(
            model_name='minutes',
            name='notes',
            field=models.FileField(upload_to='minutes/'),
        ),
    ]

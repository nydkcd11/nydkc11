# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_delete_dtc'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170706_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='event_choices',
            field=models.CharField(choices=[(b'DIV', b'Division Events'), (b'FUND', b'Fundraisers'), (b'CLUB', b'Club Events')], default=b'FUND', max_length=4, verbose_name=b'Type of Event'),
        ),
    ]

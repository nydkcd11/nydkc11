# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 00:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='message',
        ),
    ]

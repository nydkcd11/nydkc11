# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 23:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20170630_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer2',
            field=ckeditor.fields.RichTextField(default=2),
            preserve_default=False,
        ),
    ]

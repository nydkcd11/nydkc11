# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 21:14
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_school_newsletter_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer3',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=2),
            preserve_default=False,
        ),
    ]

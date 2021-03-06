# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20170712_2245'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
                ('posts', models.ManyToManyField(blank=True, related_name='posts', to='blog.Post')),
            ],
        ),
    ]

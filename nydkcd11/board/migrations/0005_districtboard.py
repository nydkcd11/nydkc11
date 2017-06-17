# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-10 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20170604_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=75)),
                ('position', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
    ]
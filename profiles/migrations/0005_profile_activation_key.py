# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-23 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20170910_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

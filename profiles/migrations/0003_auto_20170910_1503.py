# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-10 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170910_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='follower',
            new_name='followers',
        ),
    ]

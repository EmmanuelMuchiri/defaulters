# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-14 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='profpic',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_auto_20181121_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('is_admin', 'Is Admin  '), ('is_user', 'Is User'))},
        ),
    ]
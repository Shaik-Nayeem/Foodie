# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0013_auto_20181121_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]

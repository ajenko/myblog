# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171017_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Height of field'),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Width of field'),
        ),
    ]

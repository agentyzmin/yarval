# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-05 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_auto_20170806_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardata',
            name='bat',
            field=models.FloatField(),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 20:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20170319_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollutionconfig',
            name='added',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='pollutionconfig',
            name='valid_since',
            field=models.DateTimeField(default=datetime.datetime.utcnow, null=True),
        ),
    ]

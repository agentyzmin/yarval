# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_pollution'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SensorConfig',
            new_name='PollutionConfig',
        ),
        migrations.AddField(
            model_name='pollution',
            name='bat',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]

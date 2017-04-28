# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_auto_20170319_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('auth_token', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pollution',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.Device'),
        ),
        migrations.AddField(
            model_name='pollutionconfig',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.Device'),
        ),
    ]
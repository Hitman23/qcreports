# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0005_auto_20170531_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
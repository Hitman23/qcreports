# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sync_flows',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='flow',
            name='sync_flows',
            field=models.BooleanField(default=False),
        ),
    ]
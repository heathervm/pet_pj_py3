# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0004_auto_20170413_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='pet',
            field=models.CharField(default='None', max_length=300),
        ),
    ]

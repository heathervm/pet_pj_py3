# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0017_auto_20170430_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='farrier',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
        ),
        migrations.AddField(
            model_name='farrier',
            name='phone_number',
            field=models.IntegerField(default=1234567890),
        ),
        migrations.AlterField(
            model_name='farrier',
            name='name',
            field=models.CharField(max_length=300, null='False'),
        ),
    ]

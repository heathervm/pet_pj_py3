# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0015_auto_20170424_1646'),
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
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(default=1234567890),
        ),
        migrations.AddField(
            model_name='trainer',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
        ),
        migrations.AddField(
            model_name='veterinarian',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
        ),
        migrations.AddField(
            model_name='veterinarian',
            name='phone_number',
            field=models.IntegerField(default=1234567890),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
        ),
    ]

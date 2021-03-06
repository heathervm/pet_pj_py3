# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0014_auto_20170422_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='horse',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='pet_project.Horse'),
        ),
        migrations.AddField(
            model_name='plan',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendar',
            name='date',
            field=models.DateTimeField(blank='False', editable='True'),
        ),
    ]

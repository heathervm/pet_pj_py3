# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0023_auto_20170509_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farriercare',
            name='notes',
            field=models.CharField(blank='True', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='veterinarycare',
            name='attachments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pet_project.uploadFile'),
        ),
    ]

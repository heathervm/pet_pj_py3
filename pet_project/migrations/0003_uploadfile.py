# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0002_auto_20170413_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('document', models.FileField(upload_to='Documents')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=300)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('brand', models.CharField(max_length=200)),
                ('energy_level', models.CharField(default='Medium', max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Fuck',
        ),
    ]
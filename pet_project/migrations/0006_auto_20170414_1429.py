# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0005_trainer_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(default='Unknown', max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='pet',
        ),
        migrations.AlterField(
            model_name='student',
            name='trainer',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='pet_project.Trainer'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0010_auto_20170414_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(default='Grade', max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='horse',
            name='photo',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='pet_project.uploadFile'),
        ),
        migrations.AddField(
            model_name='owner',
            name='phone_number',
            field=models.IntegerField(default=1234567890),
        ),
        migrations.AddField(
            model_name='plan',
            name='file',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='pet_project.uploadFile'),
        ),
        migrations.AddField(
            model_name='horse',
            name='breed',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='pet_project.Breed'),
        ),
    ]

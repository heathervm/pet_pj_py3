# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 03:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0016_auto_20170425_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Jane Doe', max_length=300)),
                ('address', models.CharField(blank='True', max_length=700)),
                ('email', models.EmailField(blank='True', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default='8008888888', max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.RemoveField(
            model_name='farrier',
            name='email',
        ),
        migrations.RemoveField(
            model_name='farrier',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='farrier',
            name='name',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, to='pet_project.Person'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_project.Person'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_project.Person'),
        ),
        migrations.AlterField(
            model_name='veterinarian',
            name='name',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, to='pet_project.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pet_project.PhoneModel'),
        ),
    ]

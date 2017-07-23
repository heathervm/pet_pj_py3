# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pet_project', '0020_auto_20170501_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
                ('days_ordered', models.IntegerField(blank='True', default=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_project.Brand')),
            ],
        ),
        migrations.AddField(
            model_name='veterinarycare',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='horse',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_project.Person'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, to='pet_project.Person'),
        ),
        migrations.AlterField(
            model_name='veterinarycare',
            name='attachments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pet_project.uploadFile'),
        ),
        migrations.AlterField(
            model_name='veterinarycare',
            name='visit_purpose',
            field=models.CharField(choices=[('RT', 'Routine'), ('NC', 'New Complaint'), ('FL', 'Followup'), ('PP', 'Prepurchase')], max_length=2),
        ),
    ]

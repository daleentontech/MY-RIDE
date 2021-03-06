# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 11:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160707_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=254, verbose_name='year of purchase')),
                ('make', models.CharField(max_length=254, verbose_name='vehicle make')),
                ('model', models.CharField(max_length=254, verbose_name='vehicle model')),
                ('seats', models.IntegerField(blank=True, max_length=254, verbose_name='no of seats')),
                ('type', models.CharField(choices=[('private', 'private'), ('hired', 'hired')], max_length=30, verbose_name='vehicle type')),
                ('category', models.CharField(choices=[('car', 'car'), ('bus', 'bus'), ('coaster', 'coaster'), ('Truck', 'Truck')], max_length=30, verbose_name='vehicle type')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=254, verbose_name='full name'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

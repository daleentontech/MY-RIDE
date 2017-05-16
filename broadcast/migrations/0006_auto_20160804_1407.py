# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 13:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0005_auto_20160801_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadcast',
            name='bc_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='bc time'),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='broadcast_broadcast_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
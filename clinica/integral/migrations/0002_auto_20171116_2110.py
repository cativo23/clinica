# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integral', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

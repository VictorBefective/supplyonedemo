# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_provider_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='rfc',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

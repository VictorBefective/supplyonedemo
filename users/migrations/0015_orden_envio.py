# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20160801_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='envio',
            field=models.DecimalField(decimal_places=2, default=200, max_digits=14),
            preserve_default=False,
        ),
    ]

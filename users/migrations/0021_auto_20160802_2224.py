# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20160802_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_de_pago',
            field=models.DateField(null=True),
        ),
    ]

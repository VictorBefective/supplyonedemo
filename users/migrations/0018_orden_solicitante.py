# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20160802_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='solicitante',
            field=models.CharField(default='Marketing', max_length=100),
            preserve_default=False,
        ),
    ]

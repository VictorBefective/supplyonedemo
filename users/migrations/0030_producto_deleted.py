# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20160810_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]

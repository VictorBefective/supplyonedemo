# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_orden_solicitante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='solicitante',
            new_name='area',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_precalificacioncuestionario'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalificacionOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activated', models.BooleanField(default=True)),
                ('cp1', models.BooleanField()),
                ('cp2', models.BooleanField()),
                ('cc1', models.BooleanField()),
                ('sp1', models.BooleanField()),
                ('sp2', models.BooleanField()),
                ('sp3', models.BooleanField()),
                ('c1', models.IntegerField()),
                ('c2', models.IntegerField()),
                ('c3', models.IntegerField()),
                ('orden', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Orden')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

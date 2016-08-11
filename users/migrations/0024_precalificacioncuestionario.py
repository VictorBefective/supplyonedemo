# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20160809_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreCalificacionCuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evaluacion', models.DateField()),
                ('auditor', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('ins1', models.TextField(null=True)),
                ('ins2', models.TextField(null=True)),
                ('ins3', models.TextField(null=True)),
                ('ins4', models.TextField(null=True)),
                ('ins5', models.TextField(null=True)),
                ('ins6', models.TextField(null=True)),
                ('ins7', models.TextField(null=True)),
                ('ins8', models.TextField(null=True)),
                ('inp1', models.TextField(null=True)),
                ('inp2', models.TextField(null=True)),
                ('inp3', models.TextField(null=True)),
                ('inp4', models.TextField(null=True)),
                ('inp5', models.TextField(null=True)),
                ('inp6', models.TextField(null=True)),
                ('inp7', models.TextField(null=True)),
                ('inp8', models.TextField(null=True)),
                ('dpp1', models.TextField(null=True)),
                ('dpp2', models.TextField(null=True)),
                ('sg1', models.TextField(null=True)),
                ('sg2', models.TextField(null=True)),
                ('sg3', models.TextField(null=True)),
                ('sg4', models.TextField(null=True)),
                ('sg5', models.TextField(null=True)),
                ('tec1', models.TextField(null=True)),
                ('tec2', models.TextField(null=True)),
                ('tec3', models.TextField(null=True)),
                ('tec4', models.TextField(null=True)),
                ('tec5', models.TextField(null=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Provider', unique=True)),
            ],
        ),
    ]

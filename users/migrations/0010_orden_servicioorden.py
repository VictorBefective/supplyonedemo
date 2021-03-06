# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 04:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160801_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_pago', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=14)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=14)),
                ('envio', models.DecimalField(decimal_places=2, max_digits=14)),
                ('total', models.DecimalField(decimal_places=2, max_digits=14)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Provider')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServicioOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serivicio_producto', models.CharField(max_length=100)),
                ('unidades', models.IntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=14)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=14)),
                ('descripcion', models.CharField(max_length=100)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Orden')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20170905_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='estado_pago',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='estado_cotizacion',
            field=models.IntegerField(choices=[(1, 'En Espera'), (2, 'Debe'), (3, 'Pendiente Facturacion'), (4, 'Facturada'), (5, 'Atraso')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='estado_trabajo',
            field=models.IntegerField(choices=[(1, 'Esperando'), (2, 'Trabajando'), (3, 'Terminado')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20170806_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='facturas',
            field=models.ManyToManyField(blank=True, null=True, to='erp.Factura'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='observacion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='observacion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='ot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.OT'),
        ),
    ]

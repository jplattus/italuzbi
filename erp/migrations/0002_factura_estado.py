# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-06 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='estado',
            field=models.CharField(default='recibida', max_length=20),
        ),
    ]

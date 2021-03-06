# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_auto_20170921_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(null=True)),
                ('fecha', models.DateField(null=True)),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Cotizacion')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Documento')),
            ],
        ),
        migrations.RemoveField(
            model_name='utilizado',
            name='cotizacion',
        ),
        migrations.RemoveField(
            model_name='utilizado',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='utilizado',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='utilizado',
            name='numero',
        ),
        migrations.AddField(
            model_name='utilizado',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilizado',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.Material'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilizado',
            name='trabajo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.Trabajo'),
            preserve_default=False,
        ),
    ]

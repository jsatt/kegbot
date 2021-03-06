# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kegbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('dispensed_ml', models.FloatField(default=0)),
                ('beverage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kegbot.Beverage')),
            ],
        ),
        migrations.RenameField(
            model_name='tap',
            old_name='current_volume',
            new_name='dispensed_ml',
        ),
        migrations.RenameField(
            model_name='tap',
            old_name='factor',
            new_name='pulses_per_ml',
        ),
        migrations.RenameField(
            model_name='tap',
            old_name='total_volume',
            new_name='total_ml',
        ),
        migrations.AddField(
            model_name='pour',
            name='tap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kegbot.Tap'),
        ),
    ]

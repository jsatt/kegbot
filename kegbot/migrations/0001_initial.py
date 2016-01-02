# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-02 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('abv', models.FloatField(blank=True, null=True)),
                ('ibu', models.IntegerField(blank=True, null=True)),
                ('srm', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=10)),
                ('factor', models.IntegerField(default=0)),
                ('total_volume', models.FloatField(default=0)),
                ('current_volume', models.FloatField(default=0)),
                ('beverage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kegbot.Beverage')),
            ],
        ),
    ]

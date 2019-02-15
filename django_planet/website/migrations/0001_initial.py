# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-15 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=200)),
                ('city_rank', models.IntegerField()),
                ('city_des', models.CharField(max_length=250)),
                ('city_long', models.FloatField()),
                ('city_lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Continents',
            fields=[
                ('cont_id', models.AutoField(primary_key=True, serialize=False)),
                ('cont_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=200)),
                ('country_rank', models.IntegerField()),
                ('cont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Continents')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=200)),
                ('site_des', models.CharField(max_length=250)),
                ('site_rank', models.IntegerField()),
                ('site_review', models.CharField(max_length=250)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.City')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Country'),
        ),
    ]

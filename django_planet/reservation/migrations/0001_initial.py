# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-21 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_type', models.CharField(max_length=200)),
                ('car_price', models.FloatField()),
                ('car_number', models.IntegerField()),
                ('car_image', models.ImageField(blank=True, upload_to='cars_images')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Country')),
            ],
        ),
        migrations.CreateModel(
            name='CarStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_des', models.TextField(blank=True, null=True, verbose_name='hotel description')),
                ('hotel_rank', models.IntegerField()),
                ('hotel_review', models.TextField(blank=True, null=True)),
                ('hotel_image', models.ImageField(blank=True, upload_to='hotels_images')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.City')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=200)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_price', models.FloatField()),
                ('num_of_beds', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Hotel')),
            ],
        ),
        migrations.AddField(
            model_name='carstatus',
            name='loc_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location from+', to='reservation.Location'),
        ),
        migrations.AddField(
            model_name='carstatus',
            name='loc_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location to+', to='reservation.Location'),
        ),
    ]

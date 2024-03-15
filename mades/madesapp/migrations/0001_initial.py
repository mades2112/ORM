# Generated by Django 5.0.2 on 2024-03-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('Bus_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Bus_name', models.CharField(max_length=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_station_code', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2025-01-19 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teamstats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Center', 'C'), ('Right Wing', 'RW'), ('Left Wing', 'LW'), ('Right Defense', 'RD'), ('Left Defense', 'LD'), ('Goalie', 'G')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('picture', models.CharField(max_length=200, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('birth_city', models.CharField(max_length=50, null=True)),
                ('birth_state', models.CharField(max_length=50, null=True)),
                ('birth_country', models.CharField(max_length=3, null=True)),
                ('height_inches', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(null=True)),
                ('is_rookie', models.BooleanField(null=True)),
                ('handed', models.CharField(choices=[('Right', 'R'), ('Left', 'L')], max_length=10, null=True)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teamstats.team')),
                ('position', models.ManyToManyField(to='playerstats.playerposition')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2025-01-19 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamstats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='logo',
        ),
    ]

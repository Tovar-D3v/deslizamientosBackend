# Generated by Django 4.2.23 on 2025-06-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deteccion', '0002_deslizamientosmonitoreados'),
    ]

    operations = [
        migrations.AddField(
            model_name='deslizamientosmonitoreados',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]

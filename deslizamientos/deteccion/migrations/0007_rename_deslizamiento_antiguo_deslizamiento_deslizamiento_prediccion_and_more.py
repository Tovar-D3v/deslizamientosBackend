# Generated by Django 4.2.23 on 2025-07-05 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deteccion', '0006_rename_creado_deslizamiento_fecha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deslizamiento',
            old_name='deslizamiento_antiguo',
            new_name='deslizamiento_prediccion',
        ),
        migrations.RenameField(
            model_name='deslizamiento',
            old_name='deslizamiento_nuevo',
            new_name='deslizamiento_real',
        ),
        migrations.RenameField(
            model_name='deslizamiento',
            old_name='fecha',
            new_name='fecha_deslizamiento_prediccion',
        ),
        migrations.AddField(
            model_name='deslizamiento',
            name='fecha_deslizamiento_real',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 5.1.6 on 2025-03-05 01:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_equipo_liga'),
        ('ligas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='entrenador',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='fundado_en',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='liga',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='equipos_rel', to='ligas.liga'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

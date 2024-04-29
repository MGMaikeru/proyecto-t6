# Generated by Django 5.0.4 on 2024-04-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_estado_aimentacion_event_estado_alimentacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='estado_alimentacion',
        ),
        migrations.AddField(
            model_name='event',
            name='estado_aimentacion',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='estado_extras',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='estado_transporte',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

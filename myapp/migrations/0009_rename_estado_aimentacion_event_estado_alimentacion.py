# Generated by Django 5.0.4 on 2024-04-28 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_event_estado_aimentacion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='estado_aimentacion',
            new_name='estado_alimentacion',
        ),
    ]

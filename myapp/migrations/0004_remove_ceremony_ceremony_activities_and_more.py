# Generated by Django 5.0.3 on 2024-05-01 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_ceremonyactivity_ceremony_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ceremony',
            name='ceremony_activities',
        ),
        migrations.AddField(
            model_name='ceremonyactivity',
            name='ceremony',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ceremony_activities', to='myapp.ceremony'),
        ),
        migrations.AlterField(
            model_name='ceremony',
            name='end_date',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AlterField(
            model_name='ceremony',
            name='start_date',
            field=models.DateField(default='2024-01-01'),
        ),
    ]
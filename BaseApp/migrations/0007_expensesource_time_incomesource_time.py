# Generated by Django 5.0.6 on 2024-06-12 10:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0006_remove_incomesource_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensesource',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='incomesource',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

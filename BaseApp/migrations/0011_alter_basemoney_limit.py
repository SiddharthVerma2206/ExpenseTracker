# Generated by Django 5.0.6 on 2024-06-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0010_basemoney_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemoney',
            name='limit',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

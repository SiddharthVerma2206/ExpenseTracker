# Generated by Django 5.0.6 on 2024-06-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0008_basemoney_typeofacc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemoney',
            name='typeofacc',
            field=models.CharField(choices=[('Bank Account', 'Bank Account'), ('Credit Card', 'Credit Card'), ('Cash', 'Cash')], default='Cash', max_length=20),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-22 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0006_auto_20201120_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.AddField(
            model_name='person',
            name='user_type',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Seller', 'Seller'), ('Admin', 'Admin')], default='Customer', max_length=8),
        ),
    ]

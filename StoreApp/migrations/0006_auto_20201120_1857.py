# Generated by Django 3.1.2 on 2020-11-20 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0005_deliverylocation_orderedtech_orderinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverylocation',
            old_name='user',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderinfo',
            old_name='user',
            new_name='customer',
        ),
    ]

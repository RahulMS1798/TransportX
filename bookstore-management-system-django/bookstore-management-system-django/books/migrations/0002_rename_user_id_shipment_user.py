# Generated by Django 5.0 on 2024-02-08 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='user_id',
            new_name='user',
        ),
    ]

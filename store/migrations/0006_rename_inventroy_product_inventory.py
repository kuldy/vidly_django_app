# Generated by Django 3.2.7 on 2021-09-30 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_address_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='inventroy',
            new_name='inventory',
        ),
    ]
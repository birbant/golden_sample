# Generated by Django 5.0.3 on 2024-03-04 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Employees',
        ),
    ]
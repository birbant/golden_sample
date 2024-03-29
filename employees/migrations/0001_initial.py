# Generated by Django 5.0.3 on 2024-03-04 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=100)),
                ('employee_id', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)])),
                ('department', models.CharField(choices=[('quality', 'Quality'), ('projects', 'Projects'), ('tool-house', 'Tool-house'), ('technical', 'Technical'), ('other', 'Other')], max_length=20)),
            ],
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_clients_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='hello',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

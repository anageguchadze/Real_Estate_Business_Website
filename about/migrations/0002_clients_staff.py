# Generated by Django 5.1.7 on 2025-03-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]

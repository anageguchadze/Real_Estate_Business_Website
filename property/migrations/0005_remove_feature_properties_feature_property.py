# Generated by Django 5.0.7 on 2025-03-11 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_remove_feature_property_feature_properties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='properties',
        ),
        migrations.AddField(
            model_name='feature',
            name='property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='property.property'),
            preserve_default=False,
        ),
    ]

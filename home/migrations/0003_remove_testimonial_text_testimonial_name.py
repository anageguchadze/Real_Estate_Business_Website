# Generated by Django 5.0.7 on 2025-03-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_name_testimonial_title_testimonial_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='text',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-17 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='variaton_category',
            new_name='variation_category',
        ),
    ]

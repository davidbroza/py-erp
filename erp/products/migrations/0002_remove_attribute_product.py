# Generated by Django 5.0 on 2024-03-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='product',
        ),
    ]

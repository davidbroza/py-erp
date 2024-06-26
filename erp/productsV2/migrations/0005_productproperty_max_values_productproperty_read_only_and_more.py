# Generated by Django 5.0 on 2024-04-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsV2', '0004_alter_productproperty_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productproperty',
            name='max_values',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productproperty',
            name='read_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productproperty',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]

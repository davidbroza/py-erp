# Generated by Django 5.0 on 2024-03-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_attributevalue_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattributedefinition',
            name='possible_values',
            field=models.ManyToManyField(blank=True, related_name='possible_values', to='products.attributevalue'),
        ),
        migrations.DeleteModel(
            name='ProductAttributeDefinitionValue',
        ),
    ]

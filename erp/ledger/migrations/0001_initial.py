# Generated by Django 5.0 on 2023-12-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
            ],
        ),
    ]

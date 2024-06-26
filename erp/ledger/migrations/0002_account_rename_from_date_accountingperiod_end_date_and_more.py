# Generated by Django 5.0 on 2023-12-25 08:44

import django.db.models.deletion
import djmoney.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='accountingperiod',
            old_name='from_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='accountingperiod',
            old_name='to_date',
            new_name='start_date',
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CREDIT', 'Credit'), ('DEBIT', 'Debig')], max_length=10)),
                ('amount_currency', djmoney.models.fields.CurrencyField(choices=[('GBP', 'British Pound'), ('EUR', 'Euro'), ('USD', 'US Dollar')], default=None, editable=False, max_length=3)),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=14)),
                ('date', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='ledger.account')),
            ],
        ),
    ]

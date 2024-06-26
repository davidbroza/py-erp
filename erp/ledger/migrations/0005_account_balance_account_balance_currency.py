# Generated by Django 5.0 on 2023-12-25 09:06

import djmoney.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_alter_transaction_from_account_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=djmoney.models.fields.MoneyField(decimal_places=4, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='balance_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('GBP', 'British Pound'), ('EUR', 'Euro'), ('USD', 'US Dollar')], default=None, editable=False, max_length=3, null=True),
        ),
    ]

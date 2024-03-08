from django.core.exceptions import ValidationError
from django.db import models
from djmoney.models.fields import MoneyField
# import Currency


# Create your models here.
#
class AccountingPeriod(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = MoneyField(max_digits=14, decimal_places=4, default_currency="EUR")

    def credit(self, amount):
        self.balance -= amount

    def debit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"{self.name} - {self.balance}"


class Transaction(models.Model):
    amount = MoneyField(max_digits=14, decimal_places=4, default_currency="EUR")
    description = models.CharField(max_length=128)
    long_description = models.TextField(null=True, blank=True)
    from_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="credit_transactions",
    )
    to_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="debit_transactions",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    accounting_period = models.ForeignKey(
        AccountingPeriod,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    def save(self, *args, **kwargs):
        self.from_account.credit(self.amount)
        self.to_account.debit(self.amount)

        self.from_account.save()
        self.to_account.save()

        return super().save()

    def delete(self):
        self.from_account.balance += self.amount
        self.to_account.balance -= self.amount

        self.to_account.save()
        self.from_account.save()

        super().delete()

    def __str__(self):
        return f"{self.from_account.name} -> {self.amount} -> {self.to_account.name}"

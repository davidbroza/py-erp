from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField, CurrencyField


class Company(models.Model):
    legal_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    credit_limit = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency="EUR",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.legal_name


class Address(models.Model):
    country = CountryField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"

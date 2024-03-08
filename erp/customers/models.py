from django.db import models
from djmoney.models.fields import MoneyField


class Customer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    credit_limit = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", null=True, blank=True
    )

    def __str__(self):
        return self.name


# Create your models here.

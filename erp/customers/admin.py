from django.contrib import admin
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


# Register your models here.

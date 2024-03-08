from .models import Company, Address

from django.contrib import admin


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

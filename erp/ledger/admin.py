from django.contrib import admin
from ledger.models import AccountingPeriod, Transaction, Account


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


class TransactionInline(admin.TabularInline):
    model = Transaction
    fields = ["amount", "description", "accounting_period"]
    show_change_link = True
    extra = 0


class CreditsInline(TransactionInline):
    fk_name = "from_account"
    verbose_name_plural = "Credits"
    verbose_name = "Credit"
    fields = TransactionInline.fields + ["to_account"]


class DebitsInline(TransactionInline):
    fk_name = "to_account"
    verbose_name_plural = "Debits"
    verbose_name = "Debit"
    fields = TransactionInline.fields + ["from_account"]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = [CreditsInline, DebitsInline]


@admin.register(AccountingPeriod)
class AccountingPeriodAdmin(admin.ModelAdmin):
    pass

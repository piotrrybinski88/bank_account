from django.contrib import admin

from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'account_number', 'currency', 'date_created', 'account_owner', 'balance'
    )
    readonly_fields = ('account_number', 'currency', 'date_created', 'balance')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date_of_transaction', 'account')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

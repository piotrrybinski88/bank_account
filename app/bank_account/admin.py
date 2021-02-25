from django.contrib import admin

from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'account_number', 'currency', 'date_created', 'admin_balance', 'account_owner'
    )
    readonly_fields = ('account_number', 'currency', 'date_created', 'admin_balance', 'balance')

    def admin_balance(self, obj):
        all_account_transaction = Transaction.objects.filter(
            account__account_number=obj.account_number
        ).all()
        return sum([transaction.amount for transaction in all_account_transaction])


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date_of_transaction', 'account')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

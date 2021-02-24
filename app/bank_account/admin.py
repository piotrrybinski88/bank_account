from django.contrib import admin

# Register your models here.
from django.db.models import Window, Sum, F
from django.db.models.functions import Lead


from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'currency', 'date_created', 'balance')
    readonly_fields = ('account_number', 'currency', 'date_created')

    def balance(self, obj):
        all_account_transaction = Transaction.objects.filter(
            account__account_number=obj.account_number
        ).all()
        return sum([transaction.amount for transaction in all_account_transaction])


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date_of_transaction', 'account')


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

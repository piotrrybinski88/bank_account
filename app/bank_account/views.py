from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView

from .models import Account, Transaction


class ShowAccount(LoginRequiredMixin, DetailView):
    model = Account
    context_object_name = 'account'

    def get_queryset(self):
        account_pk = self.kwargs['pk']
        account = Account.objects.filter(pk=account_pk)
        all_account_transaction = Transaction.objects.filter(
            account__pk=account_pk
        ).all()
        balance = sum([transaction.amount for transaction in all_account_transaction])

        account.update(balance=balance)

        return account


class ShowTransaction(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    ordering = ['-date_of_transaction']

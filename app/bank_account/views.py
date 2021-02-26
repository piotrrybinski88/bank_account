from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView

from .models import Account, Transaction


class ShowAccount(LoginRequiredMixin, DetailView):
    model = Account
    context_object_name = 'account'


class ShowTransaction(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    ordering = ['-date_of_transaction']

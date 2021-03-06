from random import choices
from string import digits
from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import F, Sum


class Account(models.Model):
    CURRENCY = (
        ('PLN', 'PLN'),
    )

    class Meta:
        verbose_name = "Bank Account"

    account_number = models.CharField(
        _('number of Your bank account'),
        validators=[
            RegexValidator(regex='^\d{26}$', message='Length has to be 26', code='nomatch')
        ],
        default=''.join(choices(digits, k=26)),
        max_length=26,
        unique=True
    )
    currency = models.CharField(
        _('currency'),
        max_length=6,
        choices=CURRENCY,
        default='PLN',
    )
    date_created = models.DateTimeField(
        _('Date when account was created'),
        auto_now_add=True,
    )
    account_owner = models.CharField(_('Owner of account'), max_length=12)

    @property
    def balance(self):
        return self.transaction_set.aggregate(
            balance2=Sum(F('amount'))
        )['balance2'] or Decimal(0)

    def __str__(self):
        return self.account_number


DEFAULT_ACCOUNT = 1


class Transaction(models.Model):
    class Meta:
        verbose_name = "Transaction"

    date_of_transaction = models.DateTimeField(
        _('Date of banking transaction'),
        auto_now_add=True
    )
    amount = models.DecimalField(
        _('Amount of transaction in PLN'),
        max_digits=6,
        decimal_places=2,
        default=0
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        default=DEFAULT_ACCOUNT
    )


class Profile(AbstractUser):
    pass

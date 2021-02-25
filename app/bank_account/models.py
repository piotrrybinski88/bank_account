from random import choices
from string import digits
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


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
        max_length=26
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
    balance = models.DecimalField(
        _('Money balance on account'),
        default=0,
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return self.account_number


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
    account = models.ForeignKey(Account, on_delete=models.PROTECT)


class Profile(AbstractUser):
    pass

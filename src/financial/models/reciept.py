from django.db import models
from financial.models.account import Account
from users.models import *
from financial.models import *
from django_jalali.db import models as jmodels


class Reciept(models.Model):
    p = models.CharField(
        max_length=6,
        verbose_name='پیگیری',
        null=True, blank=True
    )
    time = models.CharField(
        max_length=5,
        verbose_name='زمان',
        null=True, blank=True
    )
    date = jmodels.jDateField(
        verbose_name='تاریخ',
        null=True,
        blank=True
    )
    atm_id = models.CharField(
        max_length=9,
        verbose_name='شماره ترمینال',
        null=True,
        blank=True
    )
    recovery = models.CharField(
        max_length=12,
        verbose_name='شماره بازیابی',
        null=True,
        blank=True
    )

    from_accounts = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        verbose_name='از حساب',
        related_name='from_accounts'
    )

    to_accounts = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        verbose_name='به حساب',
        related_name='to_accounts'
    )

    amount = models.PositiveBigIntegerField(
        verbose_name='مبلغ',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "قبض"
        verbose_name_plural = "قبوض"

    def __str__(self):
        if self.date:
            return str(self.date)
        else:
            return 'No Date'

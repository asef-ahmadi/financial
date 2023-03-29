from django.db import models
from users.models import *


class Reception(models.Model):
    date = models.DateField(verbose_name='تاریخ', null=True, blank=True)
    name = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='از طرف')
    amount = models.PositiveBigIntegerField(
        verbose_name='مبلغ', null=True, blank=True)
    description = models.TextField(
        verbose_name='توضیحات', null=True, blank=True)

    class Meta:
        verbose_name = 'دریافتی'
        verbose_name_plural = 'دریافتی‌ها'

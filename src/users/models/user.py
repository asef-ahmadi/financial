from django.db import models
from financial.models.account import Account, eng_to_persian


class User(models.Model):
    f_name = models.CharField(
        max_length=128, verbose_name='نام', blank=True, null=True)
    l_name = models.CharField(
        max_length=128, verbose_name='نام‌خانوادگی', blank=True, null=True)
    job = models.CharField(
        max_length=128, verbose_name='شغل', blank=True, null=True)
    tell = models.CharField(
        max_length=13, verbose_name='تلفن', blank=True, null=True)
    payment_card = models.ForeignKey(Account,
                                     max_length=16, verbose_name='شماره', blank=True, null=True, on_delete=models.CASCADE)
    brand_name = models.CharField(
        max_length=128, verbose_name='نام تولیدی', blank=True, null=True, unique=True)
    address = models.TextField(verbose_name='آدرس', blank=True, null=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    def fa_tell(self):
        if self.tell:
            fatell = eng_to_persian(self.tell)
            p1 = fatell[:4]
            p2 = fatell[4:7]
            p3 = fatell[-4:]
            return f'{p1}-{p2}-{p3}'

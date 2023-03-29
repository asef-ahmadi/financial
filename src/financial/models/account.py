from django.db import models


class Account(models.Model):
    f_name = models.CharField(
        max_length=255,
        verbose_name='نام',
        unique=True
    )
    l_name = models.CharField(
        max_length=255,
        verbose_name='نام‌خانوادگی',
        unique=True
    )
    number = models.CharField(
        max_length=16,
        verbose_name='شماره',
        unique=True
    )

    class Meta:
        verbose_name = "حساب بانکی"
        verbose_name_plural = "حساب‌های بانکی"

    def __str__(self):
        return f"{self.f_name} {self.l_name}  |  {str(self.number)[12:16]}"

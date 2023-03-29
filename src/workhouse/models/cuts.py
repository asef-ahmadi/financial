from django.db import models
from users.models import *
from users.enum import Sizes


class Cut(models.Model):
    brand_name = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cut_brand_name',
                                   default=1, verbose_name="نام تولیدی", blank=True, null=True)
    size = models.CharField(max_length=1, verbose_name="سایز",
                            choices=Sizes.choices, default=Sizes.FREE, blank=True, null=True)
    model_name = models.CharField(
        max_length=128, verbose_name="نام مدل", blank=True, null=True)
    total_taqe = models.PositiveSmallIntegerField(
        verbose_name="تعداد کل طاقه‌ها", blank=True, null=True)
    total_taqe_khar = models.PositiveSmallIntegerField(
        verbose_name="تعداد طاقه‌های خرجکار", blank=True, null=True)
    masraf_per_car = models.PositiveSmallIntegerField(
        verbose_name="مصرف هر کار", blank=True, null=True)
    length_khat = models.PositiveSmallIntegerField(
        verbose_name="طول خط‌کشی", blank=True, null=True)
    code = models.CharField(
        max_length=4, verbose_name="کد برش", blank=True, null=True, unique=True)
    date = models.DateField(verbose_name="تاریخ", blank=True, null=True)
    type_parche = models.CharField(
        max_length=128, verbose_name="جنس پارچه", blank=True, null=True)
    total_car = models.PositiveSmallIntegerField(
        verbose_name="تعداد کل کارها", blank=True, null=True)
    total_ply = models.PositiveSmallIntegerField(
        verbose_name="تعداد کل لاها", blank=True, null=True)
    tailor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tailor',
                               default=1, verbose_name="خیاط", blank=True, null=True)

    class Meta:
        verbose_name = "برش"
        verbose_name_plural = "برش‌ها"

    def __str__(self):
        return self.code

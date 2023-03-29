from asyncio.windows_events import NULL
from django.db import models
from workhouse.models import * 


class ClothRoll(models.Model):
    cut_id = models.ForeignKey(Cut, on_delete=models.PROTECT, default=1, verbose_name='کد برش', blank=True, null=True)
    color = models.CharField(max_length=128, verbose_name='رنگ', help_text='حتما وارد شود')
    length = models.PositiveSmallIntegerField(verbose_name='طول', blank=True, null=True)
    width = models.PositiveSmallIntegerField(verbose_name='عرض', blank=True, null=True)
    ply_car = models.PositiveSmallIntegerField(verbose_name='تعداد لا', blank=True, null=True)
    total_car = models.PositiveSmallIntegerField(verbose_name='تعداد کار', blank=True, null=True)
    ply_khar = models.PositiveSmallIntegerField(verbose_name='تعداد لای خرجکار', blank=True, null=True)
    descriptions = models.TextField(verbose_name='توضیحات', blank=True, null=True)

    class Meta:
        verbose_name = "طاقه"
        verbose_name_plural = "طاقه‌ها"

    def __str__(self):
            return self.color
    
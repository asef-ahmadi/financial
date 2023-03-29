from django.contrib import admin
from financial.models import *
from financial.models.reciept import Reciept
from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'splited_number',
    ]

    def full_name(self, Account):
        return f"{Account.f_name} {Account.l_name}"

    def splited_number(self, Account):
        p1 = Account.number[0:4]
        p2 = Account.number[4:8]
        p3 = Account.number[8:12]
        p4 = Account.number[12:16]
        return f'{p1} {p2} {p3} {p4}'


@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = [
        'amount_pre',
        'date',
        'name',
    ]

    def amount_pre(seld, Reception):
        amount = str(Reception.amount)
        p3 = amount[-4:]
        p2 = amount[-7:-4]
        p1 = amount[-10:-7]
        return f'{p1},{p2},{p3} تومان'


admin.site.register(Reciept)
admin.site.register(Payment)
# admin.site.register(Reception)
# admin.site.register(Account)

from django.contrib import admin
from warehouse.models import *


# admin.site.register(ClothRoll)
@admin.register(ClothRoll)
class ClothRollAdmin(admin.ModelAdmin):
    list_display = [
        'color',
        'cut_id',
        'length',
        'ply_car',
    ]

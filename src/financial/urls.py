from django.urls import path
from .views import *

urlpatterns = [
    path('reciept/', RecieptList.as_view(), name='reciept-list'),
]

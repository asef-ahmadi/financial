from django.urls import path
from .views import *

urlpatterns = [
    path('reciept/', RecieptList.as_view(), name='reciept-list'),
    path('reciept/<int:pk>/', RecieptDetail.as_view(), name='reciept-detail'),
    path('reciept/create/', RecieptCreate.as_view(), name='reciept-create'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('cut/', CutList.as_view(), name='cut-list'),
    path('cut/create/', CutCreate.as_view(), name='cut-create'),
    path('cut/<str:code>/', CutDetail, name='cut-detail'),
]

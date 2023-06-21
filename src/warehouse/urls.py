from django.urls import path
from .views import *

urlpatterns = [
    path('clothroll/', ClothRollList.as_view(), name='clothroll-list'),
    path('clothroll/<int:pk>/', ClothRollDetail.as_view(), name='clothroll-detail'),
    path('clothroll/create/', ClothRollCreate.as_view(), name='clothroll-create'),
]

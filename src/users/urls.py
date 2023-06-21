from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('create/', UserCreate.as_view(), name='user-create'),
    path('<int:pk>/update/', UserUpdate.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
    path('delete/<int:id>', delete, name='user-delete-def'),
]

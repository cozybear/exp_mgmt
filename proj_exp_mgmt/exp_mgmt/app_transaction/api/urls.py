from django.urls import path, include
from app_transaction.api.views import ListTransactions

urlpatterns = [
    # path('add/', ),
    # path('remove/',),
    # path('update/',),
    # path('delete/'),
    path('list/', ListTransactions.as_view(), name='transaction-list'),

   
    
]
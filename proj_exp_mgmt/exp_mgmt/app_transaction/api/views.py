from rest_framework import generics
from app_transaction.models import Balance
from app_transaction.api.serializers import BalanceSerializer


class ListTransactions(generics.ListAPIView):


    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer




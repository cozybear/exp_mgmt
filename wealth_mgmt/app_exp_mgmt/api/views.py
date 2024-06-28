from django.shortcuts import render
from django.db.models import Sum, Aggregate
from app_exp_mgmt.models import Expense
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from app_exp_mgmt.api.serializers import (ExpenseSerializer, TotalExpenseSerializer,
                                          ExpenseByCategorySerializer, ExpenseByMonthSerializer)
import calendar

class AddExpense(generics.CreateAPIView):

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class DeleteExpense(generics.DestroyAPIView):

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class ExpenseDetail(APIView):

    def get(self, request, pk):
        queryset = Expense.objects.get(pk=pk)
        serializer = ExpenseSerializer(queryset)
        return(Response(serializer.data))
    

class UpdateExpense(generics.UpdateAPIView):

    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ListAllExpense(generics.ListAPIView):

    serializer_class = ExpenseSerializer()
    queryset = Expense.objects.all()


class TotalExpense(APIView):
    
    def get(self, request):
        total_expense = Expense.objects.aggregate(total_expense=Sum('expense_amount'))['total_expense']
        serializer = TotalExpenseSerializer({'total_expense': total_expense})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ExpenseByCategory(APIView):

    def get(self, request):
        expense_category_final = {}
        expense = list(Expense.objects.values('expense_category').annotate(total_expense=Sum('expense_amount')))
        for item in expense:
            expense_category_final[item['expense_category']] = item['total_expense']
        serializer = ExpenseByCategorySerializer({'expense_by_category': expense_category_final})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExpenseByMonth(APIView):

    def get(self, request, month):
        month_name = self.kwargs.get('month')
        month_number = list(calendar.month_name).index(month_name)
        total_expense = 0
        expense = Expense.objects.filter(created__month=str(month_number))
        for item in expense:
            total_expense += item.expense_amount
        serializer = ExpenseByMonthSerializer({'expense_by_month': total_expense})
        return Response(serializer.data, status=status.HTTP_200_OK)
            
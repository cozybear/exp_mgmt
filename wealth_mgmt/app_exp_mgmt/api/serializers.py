from rest_framework import serializers
from app_exp_mgmt.models import Expense
from django.db.models import Sum
from rest_framework.response import Response


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"

    
class TotalExpenseSerializer(serializers.Serializer):

    total_expense = serializers.IntegerField()


class ExpenseByCategorySerializer(serializers.Serializer):
    
    expense_by_category = serializers.CharField(max_length=20)


class ExpenseByMonthSerializer(serializers.Serializer):

    expense_by_month = serializers.CharField()
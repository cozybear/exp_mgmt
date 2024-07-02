from rest_framework import serializers
from app_exp_mgmt.models import Expense, ExpenseCategoryChoice
from django.db.models import Sum
from rest_framework.response import Response


class ExpenseCategoryChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseCategoryChoice
        fields = "__all__"


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
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExpenseCategoryChoice(models.Model):

    expense_category = models.CharField(max_length=20)

    def __str__(self):
        return self.expense_category


class Expense(models.Model):

    expense_category_choices = [
                                ("PER", "PERSONAL"),
                                ("MED", "MEDICAL"),
                                ("OFF", "OFFICE"),
                                ("STN", "STATIONARY"),
                                    
    ]

    expense_amount = models.IntegerField()
    expense_name = models.CharField(max_length=30)
    #expense_category = models.CharField(max_length=20, choices=expense_category_choices)
    expense_category = models.ForeignKey(ExpenseCategoryChoice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense_name + " | " + str(self.expense_amount) + " | " + self.expense_category
    


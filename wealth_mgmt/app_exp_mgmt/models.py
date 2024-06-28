from django.db import models

# Create your models here.


class Expense(models.Model):

    expense_category_choices = [
                                ("PER", "PERSONAL"),
                                ("MED", "MEDICAL"),
                                ("OFF", "OFFICE"),
                                ("STN", "STATIONARY"),
                                    
    ]

    expense_amount = models.IntegerField()
    expense_name = models.CharField(max_length=30)
    expense_category = models.CharField(max_length=20, choices=expense_category_choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
from django.contrib import admin
from app_exp_mgmt.models import Expense, ExpenseCategoryChoice

# Register your models here.

admin.site.register(Expense)
admin.site.register(ExpenseCategoryChoice)
from django.urls import path, include
from app_exp_mgmt.api.views import (AddExpense, ListAllExpense,
                                    TotalExpense, ExpenseByCategory,
                                    ExpenseByMonth, DeleteExpense,
                                    ExpenseDetail, UpdateExpense,
                                    AddExpenseCategory, ListExpenseCategory)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#from app_exp_mgmt.api import urls

urlpatterns = [
    
    path('addexpense/', AddExpense.as_view(), name='add-expense'),
    path('<int:pk>/deleteexpense/', DeleteExpense.as_view(), name='delete-expense'),
    path('<int:pk>/update/', UpdateExpense.as_view(), name='update-expense'),
    path('<int:pk>/detail/', ExpenseDetail.as_view(), name='expense-detail'),
    path('listall/', ListAllExpense.as_view(), name='list-expense'),
    path('total/', TotalExpense.as_view(), name='total-expense'),
    path('bycategory/', ExpenseByCategory.as_view(), name='expense-by-category'),
    path('bymonth/<str:month>/', ExpenseByMonth.as_view(), name='expense-by-month'),
    path('addcategory/', AddExpenseCategory.as_view(), name='add-category'),
    path('listcategory/', ListExpenseCategory.as_view(), name='list-category'),

    

]
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Landing , name="Landing"),
    path("HomePage" , views.homePage , name="homePage"),
    path("finance" , views.financeview , name="financeurl"),
    path("baseMoney" , views.addbaseMoney , name="baseMoney"),
    path("income" , views.addincomesource , name="incomeSource"),
    path("Expense" , views.addexpensesource , name="expenseSource"),
    path("accounts" , views.showaccounts , name="showaccounts"),
    path("reset/<baseMoney_id>" , views.resetspent , name="reset-spent"),
    path("delete/<baseMoney_id>" , views.deletebaseMoney , name="delete-baseMoney"),
    path("deleteinco/<income_id>" , views.deleteincome , name="delete-income"),
    path("deleteexpo/<expense_id>" , views.deleteexpense , name="delete-expense"),
]

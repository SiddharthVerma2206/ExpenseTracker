from django.urls import path
from . import views

urlpatterns = [
    path("projects/ExpenseTracker/" , views.homePage , name="homePage"),
    path("projects/ExpenseTracker/finance" , views.financeview , name="financeurl"),
    path("projects/ExpenseTracker/baseMoney" , views.addbaseMoney , name="baseMoney"),
    path("projects/ExpenseTracker/income" , views.addincomesource , name="incomeSource"),
    path("projects/ExpenseTracker/Expense" , views.addexpensesource , name="expenseSource"),
    path("projects/ExpenseTracker/accounts" , views.showaccounts , name="showaccounts"),
    path("projects/ExpenseTracker/reset/<baseMoney_id>" , views.resetspent , name="reset-spent"),
    path("projects/ExpenseTracker/delete/<baseMoney_id>" , views.deletebaseMoney , name="delete-baseMoney"),
    path("projects/ExpenseTracker/deleteinco/<income_id>" , views.deleteincome , name="delete-income"),
    path("projects/ExpenseTracker/deleteexpo/<expense_id>" , views.deleteexpense , name="delete-expense"),
]

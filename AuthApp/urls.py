from django.urls import path 
from . import views

urlpatterns = [
    path("" , views.signup , name="signup"),
    path("projects/ExpenseTracker/login" , views.login_user , name="login"),
    path("projects/ExpenseTracker/logout" , views.logout_user  , name="logout"),
]

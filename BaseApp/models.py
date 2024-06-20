from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class baseMoney(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField(null=True, blank=True)
    Bank_Account = 'Bank Account'
    Credit_Card = 'Credit Card'
    Cash = 'Cash'

    Account_choices = [
        (Bank_Account, 'Bank Account'),
        (Credit_Card, 'Credit Card'),
        (Cash, 'Cash'),
    ]

    typeofacc = models.CharField(max_length=20 , choices=Account_choices , default=Cash)
    limit = models.IntegerField(null=True, blank=True)
    spent = models.IntegerField(blank=True , default=0)

    def __str__(self):
        return self.name 


class incomeSource(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    creditedIn = models.ForeignKey(baseMoney , on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name

class expenseSource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    debitedFrom = models.ForeignKey(baseMoney , on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name

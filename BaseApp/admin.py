from django.contrib import admin
from .models import baseMoney , incomeSource , expenseSource
# Register your models here.

admin.site.register(baseMoney)
admin.site.register(incomeSource)
admin.site.register(expenseSource)

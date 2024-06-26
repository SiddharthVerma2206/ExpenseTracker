from .models import baseMoney , incomeSource , expenseSource
from django.shortcuts import render , redirect 
from django.contrib import messages
from django.utils import timezone , dateformat
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Value, CharField , Sum
from django.db.models.functions import Concat


# Create your views here.
def homePage(request):
    if request.user.is_authenticated:
        user = request.user
        
        # Handle date filtering
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        
        if start_date and end_date:
            start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            start_date = timezone.now().date() - timezone.timedelta(days=30)
            end_date = timezone.now().date()
        
        total_income = incomeSource.objects.filter(user=user, date__range=[start_date, end_date]).aggregate(total=Sum('amount'))['total'] or 0
        total_expenses = expenseSource.objects.filter(user=user, date__range=[start_date, end_date]).aggregate(total=Sum('amount'))['total'] or 0

        combined_queryset_forsum = get_combined_queryset_forSummary(user, start_date, end_date)
        combined_queryset = get_combined_queryset(user)
        
        accounts = baseMoney.objects.filter(user=user)
        today_date = dateformat.format(timezone.now(), 'Y-m-d')
        

        context = {
            'entries': combined_queryset_forsum,
            'entriesfortable': combined_queryset,
            'user': user,
            'accounts': accounts,
            'today_date': today_date,
            'total_income': total_income,
            'total_expenses': total_expenses,
            'start_date': start_date,
            'end_date': end_date,
        }
        return render(request, 'homePage.html', context)
    else:
        return render(request, "Landing.html")

def financeview(request):
    if request.user.is_authenticated:

        income_list = incomeSource.objects.filter(user=request.user).order_by('-date', '-time')

        expense_list = expenseSource.objects.filter(user=request.user).order_by('-date', '-time')

        username = request.user
        accounts = baseMoney.objects.filter(user=request.user)
        today_date = dateformat.format(timezone.now(), 'Y-m-d')
        return render(request, 'finance/finance.html', {
            'income_page_obj': income_list,
            'expense_page_obj': expense_list,
            'user': username,
            'accounts': accounts, 
            'today_date': today_date
        })
    else:
        return redirect('homePage')
    
def showaccounts(request):
    if request.user.is_authenticated:
        bankacc = baseMoney.objects.filter(user=request.user , typeofacc = baseMoney.Bank_Account)
        cash = baseMoney.objects.filter(user=request.user , typeofacc = baseMoney.Cash)
        creditcard = baseMoney.objects.filter(user=request.user , typeofacc = baseMoney.Credit_Card)
        return render(request , 'finance/accounts.html' , {'cash':cash , 'bankAcc':bankacc , 'creditcard':creditcard})
    else:
        return redirect('homePage')

def addbaseMoney(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        typeofacc = request.POST.get('typeofacc')
        amount = request.POST.get('amount')
        limit = request.POST.get('limit')
        if typeofacc==baseMoney.Credit_Card and limit<=0:
            messages.error(request , "Limit Cannot Be Empty.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif typeofacc!= baseMoney.Credit_Card and amount<=0:
            messages.error(request , "Amount Cannot Be Empty.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            baseMoney.objects.create(
                user=request.user,
                name=name,
                typeofacc=typeofacc,
                amount=amount if typeofacc != baseMoney.Credit_Card else None,
                limit=limit if typeofacc == baseMoney.Credit_Card else None
            )
            messages.success(request , "Financtial Account Succesfully Created.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
def addincomesource(request):
    if request.method=='POST':
        name = request.POST.get('name')
        credited_to_id = request.POST.get('creditedTo')
        creditedto = baseMoney.objects.get(id=credited_to_id)
        amount =float(request.POST.get('amount'))
        date = request.POST.get('date')

        if creditedto.typeofacc == 'Credit Card':
            messages.error(request , "Cannot Add Income To a CreditCard")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif amount == 0:
            messages.error(request , "Amount Cannot Be Empty.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            creditedto.amount += amount
            creditedto.save()
            incomeSource.objects.create(
                user=request.user,
                name=name,
                creditedIn=creditedto,
                amount=amount,
                date=date,
            )
            messages.success(request , "Income Added.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def addexpensesource(request):
    if request.method=='POST':
        name = request.POST.get('name')
        debitedfrom_id = request.POST.get('debitedFrom')
        debitedfrom = baseMoney.objects.get(id=debitedfrom_id)
        amount =float(request.POST.get('amount'))
        date = request.POST.get('date')

        if amount==0:
            messages.success(request , "Amount Cannot Be Empty.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif debitedfrom.typeofacc == 'Credit Card':
            if debitedfrom.limit < amount :
                messages.error(request , "Cannot Spend More Than Limit")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                debitedfrom.limit -= amount
                debitedfrom.spent += amount
                debitedfrom.save()
                expenseSource.objects.create(
                    user=request.user,
                    name=name,
                    debitedFrom=debitedfrom,
                    amount=amount,
                    date=date,
                )
                messages.success(request , "Expense Added.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            if debitedfrom.amount < amount:
                messages.error(request , "Cannot Spend More Money Than Available")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                debitedfrom.amount -= amount
                debitedfrom.save()
                expenseSource.objects.create(
                    user=request.user,
                    name=name,
                    debitedFrom=debitedfrom,
                    amount=amount,
                    date=date,
                )
                messages.success(request , "Expense Added.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        

def resetspent(request , baseMoney_id):
    base = baseMoney.objects.get(pk=baseMoney_id)
    base.limit += base.spent
    base.spent = 0
    base.save()
    messages.success(request , "CreditCard Spending And Limit Reset!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def deletebaseMoney(request , baseMoney_id):
    tobedeleted = baseMoney.objects.get(pk=baseMoney_id)
    tobedeleted.delete()
    messages.success(request , "Account Successfully Deleted.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteincome(request , income_id):
    tobedeleted = incomeSource.objects.get(pk=income_id)
    dest=tobedeleted.creditedIn
    dest.amount -= tobedeleted.amount
    dest.save()
    tobedeleted.delete()
    messages.success(request , "Income Succesfully Deleted.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteexpense(request , expense_id):
    tobedeleted = expenseSource.objects.get(pk=expense_id)
    dest=tobedeleted.debitedFrom
    dest.amount += tobedeleted.amount
    dest.save()
    tobedeleted.delete()
    messages.success(request , "Expense Succesfully Deleted.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_combined_queryset(user):
    incomes = incomeSource.objects.filter(user=user).annotate(
        entry_type=Value('Income', output_field=CharField())
    ).annotate(
        source=Concat(Value(''), 'creditedIn__name', output_field=CharField())
    )
    
    expenses = expenseSource.objects.filter(user=user).annotate(
        entry_type=Value('Expense', output_field=CharField())
    ).annotate(
        source=Concat(Value(''), 'debitedFrom__name', output_field=CharField())
    )
    
    combined_queryset = incomes.union(expenses).order_by('-date' , '-time')
    return combined_queryset

def get_combined_queryset_forSummary(user, start_date, end_date):
    incomes = incomeSource.objects.filter(user=user, date__range=[start_date, end_date]).annotate(entry_type=Value('Income', output_field=CharField()))
    expenses = expenseSource.objects.filter(user=user, date__range=[start_date, end_date]).annotate(entry_type=Value('Expense', output_field=CharField()))
    combined_queryset = incomes.union(expenses).order_by('date')
    return combined_queryset
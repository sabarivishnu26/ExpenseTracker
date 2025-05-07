from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Transaction, Account
from django.db.models import Sum
import json

# Create your views here.
@login_required
def home(request):
    transcations=Transaction.objects.filter(user=request.user)
    total_income=transcations.filter(type='income').aaggregate(total=Sum('amount'))['total'] or 0
    total_expense=transcations.filter(type='expense').aaggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    context={
        'transactions': transcations,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance':balance,

    }
    return render(request, 'home.html', context)

@login_required
def income_view(request):
    income_transcation = Transaction.objects.filter(user=request.user,type='income')
    return render(request, 'income.html',{'income_transcations':income_transcation})

@login_required
def expense_view(request):
    expense_transcation = Transaction.objects.filter(user=request.user,type='expense')
    return render(request, 'income.html',{'income_transcations':expense_transcation})

@login_required
def charts_view(request):
    transactions = Transaction.objects.filter(user=request.user)

    # Income Chart Data
    income_data = transactions.filter(type='income').values('category').annotate(total=Sum('amount'))
    income_labels = [item['category'] for item in income_data]
    income_amounts = [float(item['total']) for item in income_data]

    # Expense Chart Data
    expense_data = transactions.filter(type='expense').values('category').annotate(total=Sum('amount'))
    expense_labels = [item['category'] for item in expense_data]
    expense_amounts = [float(item['total']) for item in expense_data]

    context = {
        'income_labels': json.dumps(income_labels),
        'income_data': json.dumps(income_amounts),
        'expense_labels': json.dumps(expense_labels),
        'expense_data': json.dumps(expense_amounts),
    }

    return render(request, 'charts.html', context)

@login_required
def accounts_view(request):
    accounts = Account.objects.filter(user=request.user)
    return render(request, 'accounts_cards.html', {'accounts': accounts})

def logout_view(request):
    logout(request)
    return redirect('login')
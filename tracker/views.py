from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login, authenticate
from .models import Transaction, Account
from django.db.models import Sum
import json
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm ,TransactionForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Create a new user
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage after successful login
            else:
                return redirect('login')  # Redirect to login page on failure
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


@login_required
def home(request):

    all_categories = Transaction.objects.filter(user=request.user).values_list('category', flat=True).distinct()
    selected_category = request.GET.get('category')

    # Apply category filter if selected
    transcations = Transaction.objects.filter(user=request.user)

    if selected_category:
        transcations = transcations.filter(category=selected_category)
    total_income=Transaction.objects.filter(type='income',user=request.user).aggregate(total=Sum('amount'))['total'] or 0
    total_expense=Transaction.objects.filter(type='expense',user=request.user).aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    context={
        'transactions': transcations,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance':balance,
        'all_categories': all_categories,
        'selected_category': selected_category,

    }
    return render(request, 'home.html', context)

@login_required
def income_view(request):
    income_transcation = Transaction.objects.filter(type='income',user=request.user)
    context={
            'income_transcations':income_transcation,
    }
    return render(request, 'income.html',context)

@login_required
def expense_view(request):
    expense_transcation = Transaction.objects.filter(type='expense',user=request.user)
    context={
            'expense_transcations':expense_transcation,
    }
    return render(request, 'expense.html',context)

@login_required
def edit_transactions_view(request,pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'edit_transaction.html', {'form': form})

def delete_transaction_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'transaction': transaction})


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
    return render(request, 'accounts&cards.html', {'accounts': accounts})

def logout_view(request):
    logout(request)
    return redirect('login')
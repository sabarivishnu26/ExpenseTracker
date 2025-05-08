from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=100,choices=[('food', 'Food'), ('rent', 'Rent'), ('travel', 'Travel'), ('others', 'Others'),('salary', 'Salary'),('Scholarship', 'scholarship')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type.capitalize()} - {self.amount}"


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50, choices=[('debit', 'Debit'), ('credit', 'Credit'), ('upi', 'UPI')])
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.bank_name} - {self.card_type}"

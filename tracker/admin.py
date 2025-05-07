from django.contrib import admin
from .models import Account,Transaction
# Register your models here.

admin.site.register(Transaction)
admin.site.register(Account)
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),  
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),  
    path('', views.home, name='home'),
    path('transaction/edit/<int:pk>/', views.edit_transactions_view, name='edit_transaction'),
    path('transaction/delete/<int:pk>/', views.delete_transaction_view, name='delete_transaction'),
    path('income/', views.income_view, name='income'),
    path('expenses/', views.expense_view, name='expenses'),
    path('charts/', views.charts_view, name='charts'),
    path('accounts/', views.accounts_view, name='accounts'),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('income/', views.income_view, name='income'),
    path('expenses/', views.expense_view, name='expenses'),
    path('charts/', views.charts_view, name='charts'),
    path('accounts/', views.accounts_view, name='accounts'),
    path('logout/', views.logout_view, name='logout'),
]

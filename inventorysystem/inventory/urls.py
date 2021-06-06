from django.urls import path
from . import views

urlpatterns = [
    path('inventory', views.inventory, name='inventory'),
    path('transactions', views.transactions, name='transactions'),
    path('transaction/register', views.register_transaction, name='transaction/register')
]
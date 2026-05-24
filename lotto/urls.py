from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_ticket, name='buy_ticket'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
]
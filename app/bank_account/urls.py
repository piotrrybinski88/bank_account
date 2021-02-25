from django.urls import path
from .views import ShowAccount, ShowTransaction

urlpatterns = [
    path('transaction', ShowTransaction.as_view(), name='account-home'),
    path('account/<str:pk>/', ShowAccount.as_view(), name='account-deatil')
]
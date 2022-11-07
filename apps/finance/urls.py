# Core Django imports
from django.urls import path

# Apps views import
from apps.finance.views import Paymentview, Callbackview

app_name = 'finance'

urlpatterns = [
    path('payment/', Paymentview.as_view(), name='payment'),
    path('callback/<int:pk>/', Callbackview.as_view(), name="callback")
]
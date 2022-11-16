# Core Django imports
from django.urls import path

# Apps views import
from apps.finance.views import Paymentview, Callbackview, Successview, Cancleview, my_webhook_view

app_name = 'finance'

urlpatterns = [
    path('payment/', Paymentview.as_view(), name='payment'),
    path('callback/<int:pk>/', Callbackview.as_view(), name='callback'),
    path('payment-success/', Successview.as_view(), name='payment-success'),
    path('payment-cancle/', Cancleview.as_view(), name='payment-cancle'),
    path('webhook/stripe', my_webhook_view, name='webhook-stripe'),


]
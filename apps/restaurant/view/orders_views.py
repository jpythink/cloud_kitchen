# django core import
from django.shortcuts import render, redirect

# django generic view import
from django.views.generic import View

# django app model import
from apps.restaurant.models import Food, Order
from apps.authentication.models import CustomUsers

# Order View
class OrderView(View):

    def get(self , request ):
        customer = request.user.id
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'order/orders.html', {'orders' : orders})
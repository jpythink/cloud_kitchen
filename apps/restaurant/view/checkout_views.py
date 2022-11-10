# Django core import
from django.shortcuts import render, redirect

# Django generic view import
from django.views.generic import View

# Apps model import
from apps.authentication.models import CustomUsers
from apps.restaurant.models import Order
from apps.finance.models import Transaction

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Check Out View
class CheckOutView(LoginRequiredMixin, View):

    login_url = 'authentication:login'
    redirect_field_name = 'check_out'

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.user.id
        cart = request.session.get('cart')
        foods = (list(cart.keys()))
        print(address, phone, customer, cart, foods)
        request.session['address'] = address
        request.session['phone'] = phone
        request.session['customer'] = customer
        request.session['cart'] = cart
        request.session['foods'] = foods
        
        return redirect('finance:payment')
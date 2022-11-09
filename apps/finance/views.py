# Django core import
from django.shortcuts import render , redirect

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin

#Apps Model Import 
from apps.restaurant.models import Food

# Generic views imports
from django.views.generic import CreateView, View, DeleteView, UpdateView

class Paymentview(View, LoginRequiredMixin):
    template_name = "finance/payment.html"

    def get(self, request):
        address = request.session.get('address')
        phone = request.session.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        # foods = 
        foods = Food.get_foods_by_id(request.session.get('foods'))
        print("This is the finance app ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>>>>>")
        print(address, phone, customer, cart, foods)
        details =  [address, phone, customer, cart, foods]
        return render(request, self.template_name,{ 'details' :details})

class Callbackview(View, LoginRequiredMixin):
    template_name = "finance/callback.html"

    def get(self, request):
        return render(request, self.template_name)
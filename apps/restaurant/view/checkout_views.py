# Django core import
from django.shortcuts import render, redirect

# Django generic view import
from django.views.generic import View

# Apps model import
from apps.authentication.models import CustomUsers
from apps.restaurant.models import Food, Order
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
        foods = Food.get_foods_by_id(list(cart.keys()))
        print(address, phone, customer, cart, foods)

        

        # if 
        for food in foods:
            print(cart.get(str(food.id)))
            order = Order(customer=CustomUsers(id=customer),
                        food=food,
                        price=food.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(food.id)))
            order.save()
        request.session['cart'] = {}
        return redirect('restaurant:cart')
        # else :
            # print("not good ")


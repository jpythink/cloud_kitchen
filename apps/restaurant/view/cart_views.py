# Django core import
from django.shortcuts import render , redirect

# Django generic view import
from django.views.generic import View

# App model import
from apps.restaurant.models import Food

# Cart View import
class CartView(View):
    def get(self, request):
         
        if request.session.get('cart') == None:
            return redirect('restaurant:restaurant_index')
        else:
            ids = list(request.session.get('cart').keys())
            foods = Food.get_foods_by_id(ids)
            return render(request , 'cart/cart.html', {'foods': foods})


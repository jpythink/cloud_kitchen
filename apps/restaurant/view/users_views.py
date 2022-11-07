# django core imports
from django.http import JsonResponse
from django.shortcuts import render, redirect

# apps models imports
from apps.restaurant.models import Food, FoodCategory, Restaurant

# python core import
import json

# Generic views imports
from django.views.generic import View

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# restaurant & food show view
class RestaurantIndexView(View):

    def post(self, request):
        food = request.POST.get("food")
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(food)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(food)
                    else:
                        cart[food] = quantity-1
                else:
                    cart[food] = quantity+1
            else:
                cart[food] = 1
        else:
            cart = {}
            cart[food] = 1
        
        request.session['cart'] = cart    
        return redirect('/restaurant-index/')


    def get(self, request):
            cart = request.session.get('cart')
            if not cart:
                request.session.cart = {}

            restaurant_id = request.GET.get('restaurant', None)
            print("restaurant_id ::::::::::::::::",restaurant_id)
            food_category_id = request.GET.get('food_category', None)

            food_category = None
            food = None

            if restaurant_id:
                get_restaurant = Restaurant.objects.get(id=restaurant_id)
                food_category = FoodCategory.objects.filter(restaurant = get_restaurant)

            if food_category_id:
                get_food_category = FoodCategory.objects.get(id=food_category_id)
                food = Food.objects.filter(food_category=get_food_category)

            restaurant = Restaurant.objects.all()

            foods = None
            food_categorys  = FoodCategory.get_all_food_categorys()
            
            food_category_id = request.GET.get('food_category')
            if food_category_id:
                foods = Food.get_all_foods_by_food_category_id(food_category_id)
            else:
                foods = Food.get_all_foods()    
            data = {}

            data['foods'] = foods
            data['food_categorys'] = food_categorys
            
            data['food_category'] = food_category
            data['food'] = food
            data['restaurant'] = restaurant
            
            return render(request, 'restaurant/new_food.html', data)


# def get_food_category(request, **kwargs):
#     if request.method == 'GET':  
#         restaurant_id = request.GET.get('restaurant_id')
#         print(restaurant_id)
#         value = {
#             'restaurant_id':restaurant_id
#         }
#         return json.dumps(value)

# def load_food_category(request):
   
#     return render(request, 'restaurant/food_category_dropdown_list.html', {'food_category':food_category})


    # def get(self, request):
    #     cart = request.session.get('cart')
    #     if not cart:
    #         request.session.cart = {}

    #     restaurant = Restaurant.objects.all()
    #     data = {}
    #     data['restaurant'] = restaurant
    #     return render(request, 'restaurant/food0.html', data)



    
# class GetRestaurentView(View):
#     def get(self, request):
#         restaurant_id = request.GET.get("restaurant")
#         food_category = None
#         food = None
#         if restaurant_id:
#             get_restaurant = Restaurant.objects.get(id=restaurant_id)
#             food_category = list(FoodCategory.objects.filter(restaurant = get_restaurant).values("name","id"))

#         data = {}
#         data['food_category'] = food_category
#         return JsonResponse(data)

# class GetFoodCategoryView(View):
#     def get(self, request):
#         food_category_id = request.GET.get('food_category')

#         if food_category_id:
#             get_food_category = FoodCategory.objects.get(id=food_category_id)
#             foods = list(Food.objects.filter(food_category=get_food_category).values(
#                 'name',
#                 'price',
#                 'food_category',
#                 'description',
#                 'image',
#                 'id',
#             ))

#         data = {}
#         data['foods'] = foods
#         print(data)
#         return JsonResponse(data)
      






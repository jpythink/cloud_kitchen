# Core Django imports
from django.urls import path

# apps views imports
# from apps.restaurant.view.users_views import GetFoodCategoryView, RestaurantIndexView, GetRestaurentView
from apps.restaurant.view.users_views import RestaurantIndexView
from apps.restaurant.view.cart_views import CartView
from apps.restaurant.view.checkout_views import CheckOutView
from apps.restaurant.view.orders_views import OrderView

users_urlpatterns = [
    path('restaurant-index/', RestaurantIndexView.as_view(), name='restaurant_index'),
    # path('get-restaurant/', GetRestaurentView.as_view(), name='get_restaurant'),
    # path('get-food-category/', GetFoodCategoryView.as_view(), name='get_food_category'),
    path('cart', CartView.as_view() , name='cart'),
    path('check-out', CheckOutView.as_view() , name='check_out'),
    path('orders', OrderView.as_view() , name='orders'),
]
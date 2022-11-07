# Core Django imports
from django.urls import path

# Apps views import
from apps.restaurant.view.dashboard_views import (DashboardIndexView, IndexView, UpdateUsersProfileView, RestaurantListView,
RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView, 
FoodCategoryCreateView, FoodCategoryListView, FoodCategoryUpdateView,
FoodCategoryDeleteView, FoodCreateView, FoodListView, FoodUpdateView, FoodDeleteView,
OrderListView, OrderUpdateView, RestaurantPasswordChangeView, restaurant_password_success)

# Apps urls import
from apps.restaurant.url.users_urls import users_urlpatterns

app_name = 'restaurant'


urlpatterns = users_urlpatterns +   [
    # password urls
    path('restaurant-user-change-password/', RestaurantPasswordChangeView.as_view(template_name = "authentication/admin_password_change.html"), name="restaurant_user_change_password"),
    path('restaurant-user-password-success/', restaurant_password_success, name="restaurant_user_password_success"),

    # update profile url
    path('update-restaurant-user/<int:pk>/', UpdateUsersProfileView.as_view(), name='update_restaurant_user_profile'),
    
    # restaurant urls
    path('restaurant-createview/', RestaurantCreateView.as_view(), name='restaurant_createview'),
    path('restaurant-list/', RestaurantListView.as_view(), name='restaurant_listview'),
    path('restaurant-update/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant_updateview'),
    path('restaurant-delete/<int:pk>/', RestaurantDeleteView.as_view(), name='restaurant_deleteview'),

    # food category urls
    path('food-category-createview/', FoodCategoryCreateView.as_view(), name='food_category_createview'),
    path('food-category-listview/', FoodCategoryListView.as_view(), name='food_category_listview'),
    path('food-category-updateview/<int:pk>/', FoodCategoryUpdateView.as_view(), name='food_category_updateview'),
    path('food-category-deleteview/<int:pk>/', FoodCategoryDeleteView.as_view(), name='food_category_deleteview'),

    # food urls
    path('food-createview/', FoodCreateView.as_view(), name='food_createview'),
    path('food-listview/', FoodListView.as_view(), name='food_listview'),
    path('food-updateview/<int:pk>/', FoodUpdateView.as_view(), name='food_updateview'),
    path('food-deleteview/<int:pk>/', FoodDeleteView.as_view(), name='food_deleteview'),

    # order urls
    path('order-listview/', OrderListView.as_view(), name='order_listview'),
    path('order-updateview/<int:pk>/', OrderUpdateView.as_view(), name='order_updateview'),

    # dashboard url
    path('dashboard_page/', DashboardIndexView.as_view(), name='dashboard_page'),
    
    path('', IndexView.as_view(), name='homepage'),
]  
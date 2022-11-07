# django core import
from django.contrib import admin

# django apps model import
from apps.restaurant.models import Food,FoodCategory, Restaurant, Order

class AdminRestaurant(admin.ModelAdmin):
    list_display = ['id','name', 'user_id', 'description', 'location', 'status']


class AdminFood(admin.ModelAdmin):
    list_display = ['name', 'price', 'food_category','description']


class AdminFoodCategory(admin.ModelAdmin):
    list_display = ['name']

    
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'food', 'customer', 'quantity', 'price']
    
    
# Register your models here.
admin.site.register(Food, AdminFood)
admin.site.register(FoodCategory, AdminFoodCategory)
admin.site.register(Restaurant, AdminRestaurant)
admin.site.register(Order, AdminOrder)
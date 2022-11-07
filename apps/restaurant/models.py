# Django core import
from django.db import models

# Apps model import
from apps.authentication.models import CustomUsers
from apps.base.base_model import BaseModel
from apps.base.choices import RestaurantStatusType, StatusType

# phonenumber field import
from phonenumber_field.modelfields import PhoneNumberField

# Python core import
import datetime

# Restaurant models here.
class Restaurant(BaseModel):
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE )
    name = models.CharField(max_length=70, unique=True)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    location = models.CharField(max_length=70, null=False, blank=False)
    status = models.IntegerField("RestaurantStatusType", choices=RestaurantStatusType.choices, default=RestaurantStatusType.OPEN)
    
    class Meta:
        db_table = 'restaurant'
        
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_restaurant():
        return Restaurant.objects.all()

    
# Food Category models here.
class FoodCategory(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    
    
    class Meta:
        db_table = 'food_category'
        
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_food_categorys():
        return FoodCategory.objects.all()    

    @staticmethod
    def get_all_food_categorys_by_restaurant_id(restaurant_id):
        if restaurant_id:
            return FoodCategory.objects.filter(restaurant = restaurant_id)
        else:
            return FoodCategory.get_all_food_categorys();


 # Food models here.   
class Food(BaseModel):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='food')
    
    class Meta:
        db_table = 'food'
        
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_foods_by_id(ids):
        return Food.objects.filter(id__in = ids)

    @staticmethod
    def get_all_foods():
        return Food.objects.all()
    
    @staticmethod
    def get_all_foods_by_food_category_id(food_category_id):
        if food_category_id:
            return Food.objects.filter(food_category = food_category_id)
        else:
            return Food.get_all_foods();
    

# Order models here
class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUsers,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = PhoneNumberField(blank=True, region="IN")
    date = models.DateField(default=datetime.datetime.today)
    status = models.IntegerField("StatusType", choices=StatusType.choices, default=StatusType.PENDING_ORDER)

    
    class Meta:
        db_table = 'order'

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


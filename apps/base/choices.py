# django core import
from django.db import models

# user type choices
class UserType(models.IntegerChoices):
    AS_USER = 0, ('as_user')
    AS_RESTAURANT = 1, ('as_restaurant')

    __empty__ = ('SELECT')

# restaurant status choices 
class RestaurantStatusType(models.IntegerChoices):
    OPEN = 0, ('open')
    CLOSE = 1, ('close')

    __empty__ = ('SELECT')

# status type choices
class StatusType(models.IntegerChoices):

    PENDING_ORDER = 0, ('Pending Order')
    ORDER_ACCEPTED = 1, ('Order Accepted')
    PERPARING_FOOD = 2, ('Perparing Food')
    FOOD_ON_THE_WAY = 3, ('Food On The Way')
    DELIVERED = 4, ('Delivered')

    __empty__ = ('SELECT')

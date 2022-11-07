#Django core 
from django.db import models

# Django auth user model
from django.contrib.auth.models import AbstractUser

# Base model
from apps.base.choices import UserType

# phone number field import
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUsers(AbstractUser):
     phone = PhoneNumberField(blank=True, region="IN")
     dob = models.DateField(null=True)
     age = models.CharField(max_length=3,default=0)
     address = models.TextField(null=True, blank=True)
     pincode = models.CharField(max_length=6,null=True, blank=True, default=000000)
     user_type = models.IntegerField("UserType", choices=UserType.choices, default=UserType.AS_USER)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
   

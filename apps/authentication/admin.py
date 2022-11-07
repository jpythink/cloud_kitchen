# Django core imports
from django.contrib import admin

# Apps model imports
from apps.authentication.models import CustomUsers


# Register your models here.
class AdminCustomUsers(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','phone', 'dob','age','address', 'pincode']

admin.site.register(CustomUsers, AdminCustomUsers)
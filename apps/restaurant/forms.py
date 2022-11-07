# Django core forms import
from urllib import request
from django import forms

# Apps model import
from apps.restaurant.models import Restaurant, FoodCategory, Food, Order

# Base status choices import
from apps.base.choices import StatusType

# phonenumber field import
from phonenumber_field.formfields import PhoneNumberField


# Restaurant Form
class RestaurantForm(forms.ModelForm):
    STATUS=(
        ('','Enter status'),
        (0,'open'),
        (1,'close')
    )
    status= forms.ChoiceField(choices=STATUS)
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'location', 'status']

        widgets = {
        "name" : forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Restaurant Name"
            }
        ),
        "description" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Restaurant Description"
            }
        ),
        "location" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter location"
            }
        ),

    }


# Food Category Form
class FoodCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(FoodCategoryForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(user=self.request.user)

    class Meta:
        model = FoodCategory
        fields = [
            'restaurant',
            'name',
        ]


# Food Form
class FoodForm(forms.ModelForm):

    image = forms.ImageField()
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(FoodForm, self).__init__(*args, **kwargs)
        # food_category
        self.fields['food_category'].queryset = FoodCategory.objects.filter(restaurant_id__user=self.request.user)


    class Meta:
        model = Food
        fields = [
            'food_category',
            'name',
            'price',
            'description',
            'image',
        ]


# Order Form
class OrderForm(forms.ModelForm):

    status = forms.ChoiceField(choices=StatusType.choices)
    phone = PhoneNumberField(required=False ,region="IN")

    class Meta:
        model = Order
        fields = [
            'status',
            'phone',
        ]

 


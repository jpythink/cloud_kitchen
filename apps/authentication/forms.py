# Django core forms import
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

# Django auth user model import
from apps.authentication.models import CustomUsers

# phone number field import
from phonenumber_field.formfields import PhoneNumberField

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            user_email = CustomUsers.objects.filter(email=email).count()>0
            # if CustomUsers.objects.filter(email=email).exists():
            if user_email:
                raise forms.ValidationError("user is already email id exist")
            else:
                return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUsers
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


        widgets = {
        "username" : forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Username Name"
            }
        ),
        "first_name" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter First Name"
            }
        ),
        "last_name" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Last Name"
            }
        ),
        "email" : forms.EmailInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "example@gmail.com"
            }
        ),
        "password1" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
        "password2" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
    }


# Restaurants Sign Up Form
class RestaurantsSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            user_email = CustomUsers.objects.filter(email=email).count()>0
            if user_email:
                raise forms.ValidationError("user is already email id exist")
            else:
                return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.user_type = 1
            user.save()
        return user

    class Meta:
        model = CustomUsers
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


        widgets = {
        "username" : forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Username Name"
            }
        ),
        "first_name" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter First Name"
            }
        ),
        "last_name" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Last Name"
            }
        ),
        "email" : forms.EmailInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "example@gmail.com"
            }
        ),
        "password1" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
        "password2" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
    }

# Log In Form
class LoginUserForm(AuthenticationForm):


     class Meta:
        fields = ['username', 'password']

     widgets = {
        "username" : forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Username Name"
            }
        ),
        "password" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
    }


# Edit User Profile Form
class EditUsersProfileForm(forms.ModelForm):

    phone = PhoneNumberField(required=False ,region="IN")
    dob = forms.DateField(widget=forms.DateInput)
    age = forms.IntegerField()
    address = forms.Textarea()
    pincode = forms.CharField(max_length=6)
  

    class Meta:
        model = CustomUsers
        fields = [
            'phone',
            'dob',
            'age',
            'address',
            'pincode',
            ]

        widgets = {
        "phone" : forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "+91 98989 78785"
            }
        ),
        "dob" : forms.DateInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter birth date"
            }
        ),
        "age" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter Your Age"
            }
        ),
        "address" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter your address"
            }
        ),
        "pincode" : forms.TextInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Enter your pincode"
            }
        ),
    }

# Password changing form
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUsers
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
        "old_password" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
        "new_password1" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
         "new_password2" : forms.PasswordInput(
                attrs={
                "class": "form-control form-control-sm",
                "placeholder": "********"
            }
        ),
    }

    
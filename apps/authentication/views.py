# Core Django imports
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.views import PasswordChangeView

# Generic views imports
from django.views.generic import CreateView, View, DeleteView, UpdateView

# Apps forms imports
from apps.authentication.forms import (SignUpForm, LoginUserForm, RestaurantsSignUpForm,EditUsersProfileForm,
                                        PasswordChangingForm)

# Apps model imports
from apps.authentication.models import CustomUsers

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# Sign Up View
class SignUpView(SuccessMessageMixin, CreateView):
    model = CustomUsers
    form_class = SignUpForm
    success_url = reverse_lazy('authentication:login')
    template_name = 'authentication/users/signup.html'
    success_message = "User has been created, please login with your username and password"

    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Please enter details properly")
        return redirect('authentication:signup')


# Restaurants Sign Up View
class RestaurantsSignUpView(SuccessMessageMixin, CreateView):
    model = CustomUsers
    form_class = RestaurantsSignUpForm
    success_url = reverse_lazy('authentication:login')
    template_name = 'authentication/restaurants/signup.html'
    success_message = "User has been created, please login with your username and password"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Please enter details properly")
        return redirect('authentication:restaurant_signup')


# Log In View
class LogInView(View):
    form_class = LoginUserForm
    template_name = "authentication/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        try:
            data = request.POST.get('username')
            user = CustomUsers.objects.get(Q(username=data) | Q(email=data))
        except:
            messages.warning(request, 'Please creat account first of your ')
            return redirect('authentication:login')
            
        user_data = {
            'username' : user.username,
            'password' : request.POST.get('password')
        }
       
        if request.method == "POST":  
            form = LoginUserForm(request, data=user_data)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    if user.user_type == 1:
                        messages.success(
                            request, f"You are logged in as {username}")
                        return redirect('restaurant:dashboard_page')
                    else:
                         messages.success(
                            request, f"You are logged in as {username}")
                         return redirect('/')

                else:
                    messages.error(request, "Error")
            else:
                messages.error(request, "Username or password incorrect")
        form = LoginUserForm()
        return render(request, "authentication/login.html", {"form": form})


# Log Out View
class LogOutView(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        logout(request)
        messages.success(request, "User logged out")
        return redirect('/')


# Delete User View
class DeleteUserView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CustomUsers
    login_url = 'login'
    template_name = 'authentication/delete_user_confirm.html'
    success_message = "User has been deleted"
    success_url = reverse_lazy('restaurant:homepage') 


# Update User Profile View
class UpdateUsersProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUsers
    form_class = EditUsersProfileForm
    login_url = 'authentication:login'
    template_name = "authentication/edit_user_profile.html"
    success_url = reverse_lazy('restaurant:homepage')
    success_message = "User updated"
    

# Password change View
class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'authentication:login'
    success_url = reverse_lazy('authentication:password_success')


# Password success function
def password_success(request):
    return render(request, "authentication/password_change_success.html")
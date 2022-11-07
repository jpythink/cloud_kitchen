# Core Django imports
from django.urls import path

# Apps views import
from apps.authentication.views import (LogOutView, SignUpView, LogInView, RestaurantsSignUpView,
                                         DeleteUserView, UpdateUsersProfileView, PasswordChangeView,
                                         password_success )

app_name = 'authentication'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('restaurant-signup/', RestaurantsSignUpView.as_view(), name='restaurant_signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('delete-user/<int:pk>/', DeleteUserView.as_view(), name="delete_user"), 
    path('update-user/<int:pk>/', UpdateUsersProfileView.as_view(), name='update_user_profile'),
    path('change-password/', PasswordChangeView.as_view(template_name = "authentication/password_change.html"), name="change_password"),
    path('password-success/', password_success, name="password_success"),
]
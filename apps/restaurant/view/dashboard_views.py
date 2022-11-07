# Core Django imports
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView

# Generic views imports
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, TemplateView

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Apps model import
from apps.restaurant.models import Restaurant, Food, FoodCategory, Order
from apps.authentication.models import CustomUsers

# Apps forms import
from apps.restaurant.forms import RestaurantForm, FoodCategoryForm, FoodForm, OrderForm
from apps.authentication.forms import EditUsersProfileForm, PasswordChangingForm


# Dashboard User Access Permission 
class UserAccessMixin(PermissionRequiredMixin):
    def has_permission(self):
        """
        Override this method to customize the way permissions are checked.
        """
       
        user_type = self.request.user.user_type
        print('self.user: ', user_type)
        if user_type==1:
            return True
        else:
            return False
        
# Restaurant User Password Change
class RestaurantPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'authentication:login'
    success_url = reverse_lazy('restaurant:restaurant_user_password_success')

# Restaurant User  Password Change
def restaurant_password_success(request):
    return render(request, "authentication/admin_password_change_success.html")

# Restaurant User Profile Updateview
class UpdateUsersProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUsers
    form_class = EditUsersProfileForm
    login_url = 'authentication:login'
    template_name = "authentication/admin_edit_user_profile.html"
    success_url = reverse_lazy('restaurant:dashboard_page')
    success_message = "User updated"

# Restaurant Createview
class RestaurantCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm   
    login_url = 'authentication:login'
    template_name = 'restaurant/dashboard_restaurant_form.html'
    success_url = reverse_lazy('restaurant:dashboard_page')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


# Restaurant Listview 
class RestaurantListView(LoginRequiredMixin, UserAccessMixin, ListView):
    model = Restaurant
    login_url = 'authentication:login'
    template_name = 'restaurant/restaurant_list.html'
    success_url = reverse_lazy('restaurant:restaurant_listview')

    def get_queryset(self):
        return Restaurant.objects.filter(user_id=self.request.user.id)

# Restaurant Updateview
class RestaurantUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    model = Restaurant
    login_url = 'authentication:login'
    form_class = RestaurantForm
    template_name = 'restaurant/dashboard_restaurant_form.html'
    success_url = reverse_lazy('restaurant:restaurant_listview')


# Restaurant Deleteview
class RestaurantDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    model = Restaurant
    login_url = 'authentication:login'
    success_url = reverse_lazy('restaurant:restaurant_listview')


# Food Category CreateView
class FoodCategoryCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    model = FoodCategory
    form_class = FoodCategoryForm
    login_url = 'authentication:login'
    template_name = 'food_category/dashboard_food_category_form.html'
    success_url = reverse_lazy('restaurant:dashboard_page')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(FoodCategoryCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# Food Category ListView
class FoodCategoryListView(LoginRequiredMixin, UserAccessMixin, ListView):
    model = FoodCategory
    login_url = 'authentication:login'
    template_name = 'food_category/dashboard_food_category_list.html'
    success_url = reverse_lazy('restaurant:food_category_listview')

    def get_queryset(self):
         return FoodCategory.objects.filter(restaurant__user=self.request.user.id)


# Food Category Updateview
class FoodCategoryUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    model = FoodCategory
    form_class = FoodCategoryForm
    login_url = 'authentication:login'
    template_name = 'food_category/dashboard_food_category_form.html'
    success_url = reverse_lazy('restaurant:food_category_listview')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(FoodCategoryUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    

# Food Category Deleteview
class FoodCategoryDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    model = FoodCategory
    login_url = 'authentication:login'
    success_url = reverse_lazy('restaurant:food_category_listview')


# Food Create View
class FoodCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    
    model = Food
    form_class = FoodForm
    login_url = 'authentication:login'
    template_name = 'food/dashboard_food_form.html'
    success_url = reverse_lazy('restaurant:dashboard_page')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(FoodCreateView , self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# Food ListView
class FoodListView(LoginRequiredMixin, UserAccessMixin, ListView):
    model = Food
    login_url = 'authentication:login'
    template_name = 'food/dashboard_food_list.html'
    success_url = reverse_lazy('restaurant:food_listview')

    def get_queryset(self):
        return Food.objects.filter(food_category_id__restaurant_id__user=self.request.user.id)


# Food Updateview
class FoodUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    model = Food
    form_class = FoodForm
    login_url = 'authentication:login'
    template_name = 'food/dashboard_food_form.html'
    success_url = reverse_lazy('restaurant:food_listview')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(FoodUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# Food Deleteview
class FoodDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    model = Food
    login_url = 'authentication:login'
    success_url = reverse_lazy('restaurant:food_listview')

# Order Listview
class OrderListView(LoginRequiredMixin, UserAccessMixin, ListView):
    model = Order
    login_url = 'authentication:login'
    template_name = 'order/dashboard_order_list.html'
    success_url = reverse_lazy('restaurant:order_listview')

    def get_queryset(self):
        return Order.objects.filter(food__food_category__restaurant__user_id=self.request.user.id)


# Order Updateview
class OrderUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    model = Order
    form_class = OrderForm
    login_url = 'authentication:login'
    template_name = 'order/dashboard_order_form.html'
    success_url = reverse_lazy('restaurant:order_listview')


    
    


# Create index views here.
class IndexView(TemplateView):
    template_name = 'index.html'


 # Create dashboard index views here.
class DashboardIndexView(LoginRequiredMixin, UserAccessMixin, TemplateView):
    login_url = 'authentication:login'
    template_name ='base/dashboard_base.html'
    

# def index(request):
#     # foods = None
#     # food_categories  = FoodCategory.get_all_food_categorys()
#     # food_categorie_id = request.GET.get('food_categorie')
#     # if food_categorie_id:
#     #    foods = Food.get_all_foods_by_food_category_id(food_categorie_id)
#     # else:
#     #     foods = Food.get_all_foods()
#     # data = {}
#     # data['foods'] = foods
#     # data['food_categories'] = food_categories
#     return render(request, 'index.html')
    
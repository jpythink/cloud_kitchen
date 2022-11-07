# Django core import
from django.shortcuts import render , redirect

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Generic views imports
from django.views.generic import CreateView, View, DeleteView, UpdateView

class Paymentview(View, LoginRequiredMixin):
    template_name = "finance/payment.html"

    def get(self, request):
        return render(request, self.template_name,)

class Callbackview(View, LoginRequiredMixin):
    template_name = "finance/callback.html"

    def get(self, request):
        return render(request, self.template_name)
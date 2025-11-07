from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category, Product, Country, Services
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomePage(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'page-index-1.html'
    ordering = ['-created_at']
    login_url = 'login'
    redirect_field_name = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category'] = Category.objects.filter(is_active=True)
        data['country'] = Country.objects.filter(is_active=True)
        data['services'] = Services.objects.filter(is_active=True)
        data['popular'] = Product.objects.all().order_by('-review')[:3]
        data['discount'] = Product.objects.filter(discount__gt=0)[:5]
        data['recomended_products'] = Product.objects.filter(recomended=True).order_by('-review')[:18]
        data['apparel_product'] = Product.objects.filter(
            subcategory__category__name__iexact='Apparel',
            is_active=True
        )
        return data
    
class UserLoginView(LoginView):
    template_name = 'page-user-login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserRegisterView(ListView):
    model = Product
    template_name = 'page-user-register.html'

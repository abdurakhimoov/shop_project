from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category, Product, Country, Services

class HomePage(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'page-index-1.html'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category'] = Category.objects.filter(is_active=True)
        data['country'] = Country.objects.filter(is_active=True)
        data['services'] = Services.objects.filter(is_active=True)

        return data
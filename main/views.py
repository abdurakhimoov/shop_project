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
        data['popular'] = Product.objects.all().order_by('-review')[:3]
        data['discount'] = Product.objects.filter(discount__gt=0)[:5]
        data['recomended_products'] = Product.objects.filter(recomended=True).order_by('-review')[:18]
        data['apparel_product'] = Product.objects.filter(
            subcategory__category__name__iexact='Apparel',
            is_active=True
        )
        return data
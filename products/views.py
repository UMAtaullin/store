from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    data = {
        'title': 'Store',
               }
    return render(request, 'products/index.html', data)


def product(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    data = {
        'title': 'Store - Каталог',
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/products.html', data)

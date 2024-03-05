from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Basket, Product, ProductCategory


def index(request):
    data = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', data)


def product(request, category_id=None, page_number=1):
    if category_id:
        products = Product.objects.filter(category__id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    categories = ProductCategory.objects.all()
    data = {
        'title': 'Store - Каталог',
        'products': products_paginator,
        'categories': categories,
    }
    return render(request, 'products/products.html', data)


@login_required
def basket_add(request, product_id):
    """Добавление товара в корзину покупок."""
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META['HTTP_REFERER'])

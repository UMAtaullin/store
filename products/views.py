from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Basket, Product, ProductCategory


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

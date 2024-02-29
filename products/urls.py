from django.urls import path

from products.views import product

app_name = 'products'

urlpatterns = [
    path('', product, name='index'),
]

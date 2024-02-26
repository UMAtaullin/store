from django.contrib import admin
from django.urls import path

from products.views import index, product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', product, name='products'),
]

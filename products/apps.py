from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'    # Тип данных для создания таблицы.
    name = 'products'

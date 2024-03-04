from pathlib import Path

from django.conf.global_settings import AUTH_USER_MODEL, LOGIN_URL

BASE_DIR = Path(__file__).resolve().parent.parent   # Путь до корня.

SECRET_KEY = 'django-insecure-4au3(lk_rk@($uap^$^p+ggoh#m75dwoto&!e4=g!uy^0iku-n'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Управлять данными app: добавление, удаление и изменение записей в БД.
    'django.contrib.admin',
    # Oбеспечивает систему аутентификации и авторизации: управление users,
    # группами и привилегиями, а также предоставляет механизмы аутентификации,
    # такие как вход через логин/пароль или социальные сети.
    'django.contrib.auth',
    # Позволяет создавать связи между моделями
    'django.contrib.contenttypes',
    # Предоставл поддержку сессий для веб-apps, позволяет хранить данные сеанса
    # для каждого пользователя, обеспечивая сохранение состояния м/у запросами.
    'django.contrib.sessions',
    # Управления сообщениями обратной связи с пользователями.
    'django.contrib.messages',
    # Организации и обслуживании статических файлов проекта.
    'django.contrib.staticfiles',

    # tools
    'django_extensions',

    # local apps
    'products.apps.ProductsConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        # Утилита для работы с шаблонами.
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [    # Валидация для паролей. По умолчанию их 4.
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'  # Это все стили, скрипты, изображения.
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Users

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login/'

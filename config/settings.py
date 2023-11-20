from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent   # Для определения корневого каталога.

SECRET_KEY = 'django-insecure-4au3(lk_rk@($uap^$^p+ggoh#m75dwoto&!e4=g!uy^0iku-n'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Управлять данными приложения: добавление, удаление и изменение записей в БД.
    'django.contrib.admin',
    # Oбеспечивает систему аутентификации и авторизации: управление пользователями,
    # группами и привилегиями, а также предоставляет механизмы аутентификации,
    # такие как вход через логин/пароль или социальные сети.
    'django.contrib.auth',
    # Позволяет создавать связи между моделями
    'django.contrib.contenttypes',
    # Предоставляет поддержку сессий для веб-приложений, позволяет хранить данные сеанса
    # для каждого пользователя, обеспечивая сохранение состояния между запросами.
    'django.contrib.sessions',
    # Управления сообщениями обратной связи с пользователями.
    'django.contrib.messages',
    # Организации и обслуживании статических файлов проекта.
    'django.contrib.staticfiles',

    # local apps
    'products.apps.ProductsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # Безопасность.
    'django.contrib.sessions.middleware.SessionMiddleware',     # Проброска сессий для пользователей.
    'django.middleware.common.CommonMiddleware',                # ...
    'django.middleware.csrf.CsrfViewMiddleware',                # Защита от атак csrf токены.
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Аунтификацию добавляют.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',   # Утилита для работы с шаблонами.
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'  # Это все стили, скрипты, изображения.
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

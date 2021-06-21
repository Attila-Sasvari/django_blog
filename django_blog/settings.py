from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-c(qgy6q5^6ud@rt0x1a@@x9%)$go5e#6z9%k!8h1d)-73n&9!='

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'graphene_django',
    'corsheaders',
    'blog',
    'accounts',
    'api',
    'dashboard',
    'upload',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'django_blog.urls'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ("http://localhost:8080",)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'django_blog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
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

USE_L10N = True

USE_TZ = True

YEAR_CHOICES = list(range(1921, 2021))

DATE_INPUT_FORMATS = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "django_blog/static")
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFUALT_COVER_IMG = 'default_cover_img.jpg'
DEFUALT_PROFILE_IMG = 'default_profile_img.jpg'

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

GRAPHENE = {
  "SCHEMA": "blog.schema.schema",
}

LOGIN_REDIRECT_URL = '/blog'
LOGOUT_REDIRECT_URL = '/blog'

""" try:
    from .local_settings import *
except ImportError:
    print("============IMPORT error==================")
 """
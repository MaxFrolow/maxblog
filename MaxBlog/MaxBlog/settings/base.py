"""
Django settings for MaxBlog project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'po9f_yw*i+dpd2x(cnxk7l+8zwyjx6+=8e0*@ppdi*=*_)=!@8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    #librarys
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'account',
    'rest_framework_swagger',

    #my apps
    'MaxBlog.apps.MaxBlogConfig',
    'mainpage.apps.MainpageConfig',
    'accounts.apps.AccountsConfig',
    'likes.apps.LikesConfig',
    'rest.apps.RestConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'MaxBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account',
            ],
            'builtins': [
                'mainpage.templatetags.category_tags',
                'mainpage.templatetags.pagination',
            ],

        },

    },
]

WSGI_APPLICATION = 'MaxBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'test37'),
        'PORT': '5432',
        'HOST': 'db',
        'ATOMIC_REQUESTS': True
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDER_CLASSES':[
        'rest_framework.renderers.JSONRender',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
}

DJOSER = {
    'SERIALIZERS': {
        'user_registration': 'rest.accounts.serializers.UserSerializer',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/




LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    'locale',
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

STATICFILES_DIRS = ['staticfiles', ]
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

ACCOUNT_LOGIN_URL = 'MaxBlog:accounts_login'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = ACCOUNT_LOGIN_URL
ACCOUNT_PASSWORD_RESET_REDIRECT_URL = ACCOUNT_LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_URL = "MaxBlog:accounts_confirm_email"
ACCOUNT_SETTINGS_REDIRECT_URL = 'MaxBlog:accounts_settings'
ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = "MaxBlog:account_password"


EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "myemail@gmail.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SITE_ID = 1
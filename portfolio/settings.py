from logging import fatal
from pathlib import Path
import os
from django.contrib.auth.decorators import login_required
import yaml




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR , 'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#qu81gyua(_qi@gx%h9$dheu%1%jzvyr%t2bl5mi5b$x%5h!g1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if os.getenv('GAE_APPLICATION', None):
        ALLOWED_HOSTS = ['the-option-320617.de.r.appspot.com',]
else:
     DEBUG = True
     ALLOWED_HOSTS = ['*']
     import yaml
     with open(os.path.join(BASE_DIR,'secrets','secrets_dev.yaml')) as file:
        objs = yaml.safe_load(file)
        for obj in objs:
            os.environ[obj] = objs[obj]
     

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'board.apps.BoardConfig'
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

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USERNAME'],
            'PASSWORD': os.environ['DB_USER_PASSWORD'],
            'HOST': '/cloudsql/{}'.format(os.environ['DB_CONNECTION']),
        }
    }
else:
    # 開発環境
    # """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USERNAME'],
            'PASSWORD': os.environ['DB_USER_PASSWORD'],
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }    
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    """


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
PASSWORD_HASHERS = [
     'django.contrib.auth.hashers.Argon2PasswordHasher',
     'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
     'django.contrib.auth.hashers.BCryptPasswordHasher',
     'django.contrib.auth.hashers.PBKDF2PasswordHasher',
     'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]


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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'accounts.UserModel'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = 'board:list_thread'

LOGOUT_REDIRECT_URL = 'board:list_thread'

# --- Gmail 送信設定 ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
EMAIL_HOST_PASSWORD =os.environ['EMAIL_HOST_PASSWORD']

# --- DBキャッシュ設定 ---
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}
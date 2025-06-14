
from pathlib import Path
import os
import dj_database_url


# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# cloudinary.config(
#     cloud_name='dcrbyi2ka',
#     api_key='358974542787751',
#     api_secret='lM2PKTKB9cGvbpvE7yxKccvqjvs'
# )

# CLOUDINARY_STORAGE = { 
#     'CLOUD_NAME': os.environ['CLOUDINARY_CLOUD_NAME'],
#     'API_KEY': os.environ['CLOUDINARY_API_KEY'],
#     'API_SECRET': os.environ['CLOUDINARY_API_SECRET'],
# }


# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nj-n#eu$tb8&p(fxs=%z^_&7jr1093hbat*39f4v-oo%5p7l2^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [ ]

LOGIN_URL = 'login'  # Replace 'login_page' with the name of your login view





# SECRET_KEY = os.environ.get("SECRET_KEY")
# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# DATABASE_URL = os.environ.get("DATABASE_URL")
# if not DATABASE_URL:
#     raise Exception("DATABASE_URL is not set in environment variables!")

# DATABASES = {
#     "default": dj_database_url.parse(DATABASE_URL)
# }


# DATABASE_URL = "postgresql://blood_bank_i1nt_user:uEzVQsakPixYKlAMmRNgNn5rNlozSTh3@dpg-d008buqli9vc739kukfg-a.virginia-postgres.render.com/blood_bank_i1nt"
# DATABASES = {
#     "default": dj_database_url.parse(DATABASE_URL)
# }








# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'blog',
    'channels',
    # 'cloudinary',
    # 'cloudinary_storage',
    # 'storages',

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

AUTH_USER_MODEL = 'myapp.CustomUser'


ROOT_URLCONF = 'test_sm.urls'

TEMPLATES = [
    {
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

WSGI_APPLICATION = 'test_sm.wsgi.application'

ASGI_APPLICATION = 'test_sm.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases



# postgresql://blood_bank_i1nt_user:uEzVQsakPixYKlAMmRNgNn5rNlozSTh3@dpg-d008buqli9vc739kukfg-a.virginia-postgres.render.com/blood_bank_i1nt
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blood_bank',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bloodbank',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5432',

#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 86400  # 1 day
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Session expires when the browser closes
SESSION_SAVE_EVERY_REQUEST = True


EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True
<<<<<<< HEAD
EMAIL_HOST_USER="everestatnepal4ever@gmail.com"
EMAIL_HOST_PASSWORD="juwm adxs cyxk fyib"

# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
=======
# EMAIL_HOST_USER="everestatnepal4ever@gmail.com"
# EMAIL_HOST_PASSWORD=""
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
>>>>>>> 06141c9763be1d9f3a26ea41f2fee042c80cfa13



from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',  # 👈 Important for showing error in red
}




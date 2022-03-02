"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os



#CSRF_FAILURE_VIEW = "mysite"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b#s*_o(3t3ai_k(c5po@h7a=nj5#vjkd3u7ckhnx@)mi=8fn67'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#need to define
LOGIN_REDIRECT_URL = '/'
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
     'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
   'django.contrib.sites',
    'testing.apps.TestingConfig',
    #'WebAuthn.apps.WebAuthnConfig',
    'Links.apps.LinksConfig',
    'progress.apps.ProgressConfig',
    'Uploads.apps.UploadsConfig',
    'uploader.apps.UploaderConfig',

        'allauth',
    'allauth.account',
    'allauth.socialaccount',
      'allauth.socialaccount.providers.google',
  'allauth.socialaccount.providers.github',
   # 'progress.apps.WebsiteIdeasConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfauu6s2p9c2mc', 
        'USER': 'sjndilncqlgysz',
        'PASSWORD': 'e8538d5f8ee333d967cea5ec709d41be8106f14a642dbf270ef43535217c58f6',

        'HOST': 'ec2-34-230-198-12.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
       'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
     },
    {
      'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
   {
        'NAME':      
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    }
]
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
  
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, 'static-collected')

X_FRAME_OPTIONS = '*'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

 )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {

    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": "407761889721-t8n2fl5do3vdmnct8jm80aeb5g93bvs3.apps.googleusercontent.com",
 "client_secret":"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",
  
        },
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    "github": {
    "APP":{
      "client_id": "fa60c81b5821c344c7d4",
    "client_secret":"3dbea7bcb8a1b9e51574084430b3c2e2ebdbafa3",
    },
      "SCOPE": [
        "user:email"
      ]
  
      
}


  
#SOCIALACCOUNT_QUERY_EMAIL = True

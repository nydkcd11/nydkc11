"""
Django settings for nydkcd11 project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from os import path
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

with open('/etc/secret_key.txt') as f:
	SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nydkc11.org','138.197.39.225']
PROJECT_DIR_PATH = path.dirname(path.normpath(path.abspath(__file__)))

SECURE_CONTENT_TYPE_NOSNIFF= True

SECURE_BROWSER_XSS_FILTER= True

SESSION_COOKIE_SECURE= True

CSRF_COOKIE_SECURE=True

SECURE_SSL_REDIRECT=True

X_FRAME_OPTIONS='DENY'

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS=True

SECURE_HSTS_PRELOAD=True
# Application definition

CKEDITOR_CONFIGS = {
    'default':{
        'toolbar':'full',
    
	'extraPlugins':','.join(
        	[
        		'youtube',
			'image2',
        	]
    ),
   }	   
}

DATA_UPLOAD_MAX_MEMORY_SIZE=10485760
FILE_UPLOAD_MAX_MEMORY_SIZE=10485760
INSTALLED_APPS = [
	'about.apps.AboutConfig',
	'forms.apps.FormsConfig',
	'resources.apps.ResourcesConfig',
	'contact.apps.ContactConfig',
	'blog.apps.BlogConfig',
	'events.apps.EventsConfig',
	'projects.apps.ProjectsConfig',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sitemaps',
	'embed_video',
	'bootstrap3',
	'ckeditor',
	'ckeditor_uploader'
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

ROOT_URLCONF = 'nydkcd11.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR,'templates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
		'django.template.context_processors.media',
		'django.template.context_processors.static',
		'contact.context_processors.email_form',
		'projects.context_processors.projects',
		'events.context_processors.conventions',
		'contact.context_processors.number',
            ],
        },
    },
]

WSGI_APPLICATION = 'nydkcd11.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nydkc11',
        'USER': 'brian',
        'PASSWORD': 'oh12993791soo',
        'HOST': 'localhost',
        'PORT': '',
    }
}
'''
DEVELOPMENT
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
#UNLOCK IN DEVELOPMENT
#STATICFILES_DIRS= (os.path.join(BASE_DIR,'static'),)
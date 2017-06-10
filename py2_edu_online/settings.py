# coding: utf-8
"""
Django settings for py2_edu_online project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
import private

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将django的几个app放入了apps/目录下,所以需要将apps目录放入到sys.path中，以便python能正确执行
# 将xamdin放入了extrap_apps目录下，理由同上
APPS = os.path.join(BASE_DIR, 'apps')
EXTRA_APPS = os.path.join(BASE_DIR, 'extra_apps')
sys.path.insert(0, APPS)
sys.path.insert(0, EXTRA_APPS)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uc8^3t5zpg5#%=zqmm!n#qo(qi$kxo#rq!n4b8w%ojc0e5*#2a'

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

    # 自定义 app
    'global_site',
    'users',
    'courses',
    'organizations',
    'operations',

    # xamdin 
    'xadmin',
    'crispy_forms',

    # django的分页插件
    'pure_pagination',
]

# django中新建了`users`app后，使用自定义的user模型 
AUTH_USER_MODEL = 'users.USER'

# 在users.views.py文件中重写了CustomBackend的authenticate方法，支持同时使用邮箱和用户名登录
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'py2_edu_online.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/',
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'py2_edu_online.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edu_online',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# 修改语言
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
# 修改时区
TIME_ZONE = 'asia/shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
# 是否启用时区
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# 只是地址常量
STATIC_URL = '/static/'

# 定义好这个后，模板中使用{% load statickfiles %}才有效
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# 发送邮件设置，都放在django-project/private.py文件中
EMAIL_HOST = private.CUSTOM_EMAIL_HOST
EMAIL_HOST_USER = private.CUSTOM_EMAIL_USER
EMAIL_HOST_PASSWORD = private.CUSTOM_EMAIL_PASSWORD
EMAIL_FROM = private.CUSTOM_EMAIL_FROM
EMAIL_USE_TLS = False
EMAIL_PORT = 25

# media文件地址常量
MEDIA_URL = '/media/'

# django model中上传文件的存放都会放在media下
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
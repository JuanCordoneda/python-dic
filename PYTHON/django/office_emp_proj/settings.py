"""
CONTIENE TODA LA INFORMACION DE LOS ARCHIVOS DE NUESTRO PROYECTO.
ES EL ENV DE NUESTRO PROYECTO
"""
#https://platzi.com/clases/2694-django/45265-ajustando-el-archivo-settingspy/ DESDE EL MIN 6

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@gspj#ifgnpj4f&=czkn_i%knko&d-#gmz8ablf^9at4g9hr_0'

#DEBUG SIEMPRE DEBER SER FALSE EN PRODUCCION
DEBUG = True

ALLOWED_HOSTS = []


#APPS INTERNAS DE NUESTRO PROYECTO, QUE APPS ESTAN INSTALADAS

INSTALLED_APPS = [
    'django.contrib.admin', #ADMINISTRA DATOS
    'django.contrib.auth', #AUTENTICACION DE USUARIOS
    'django.contrib.contenttypes', #FORMATOS DE ARCHIVOS
    'django.contrib.sessions', #SESIONES DE USUARIOS
    'django.contrib.messages', #COMUNICACIONES ENTRE USUARIOS, FRAMEWORK DE MENSAJERIA
    'django.contrib.staticfiles', #APP PARA ARCHIVOS ESTATICOS (HTML, CSS, JAVASCRIPT)
    #CADA APP NUEVA DEBE ESTAR ACA
    'emp_app',
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

ROOT_URLCONF = 'office_emp_proj.urls'

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

WSGI_APPLICATION = 'office_emp_proj.wsgi.application'


# Database, MANEJA LAS BASES DE DATOS. CONEXION A BASES DE DATOS
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# django no soporta bases de datos no relacionales pero se pueden hackear
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #MOTOR DE LA BASE DE DATOS EN VEZ DE sqlite3, PUEDE SER mysql,postgresql,oracle
        'NAME': BASE_DIR / 'db.sqlite3',
        #para mysql tambien hay que agregar otros campos como:
        'USER':'USER',
        'PASSWORD':'PASS',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us' #EN QUE LENGUAGE ESTA CODEADO NUESTRO PROYECTO

TIME_ZONE = 'UTC' #FORMATO INTERNACIONAL

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


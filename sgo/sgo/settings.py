"""
Configurações do Django para o projeto SGO.

Gerado por `django-admin startproject` com Django 5.2.

Documentação: https://docs.djangoproject.com/en/5.2/topics/settings/
Referência completa: https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path

# Caminhos: use BASE_DIR / 'subpasta'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Ajustes rápidos para desenvolvimento — não use em produção sem revisão.
# Lista de verificação: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ATENÇÃO: em produção, use uma chave secreta forte e armazenada com segurança.
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-^e!pq99yblwp0r9*s=e+g_+72r)-5=dclo2fb5+#3fdudu@ef5',
)

# ATENÇÃO: desative DEBUG em produção.
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('1', 'true', 'yes')

_allowed = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1')
ALLOWED_HOSTS = [h.strip() for h in _allowed.split(',') if h.strip()]


# Aplicações instaladas e middleware

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'sgo_app.apps.RepairsConfig',
    'sgo_app',
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

ROOT_URLCONF = 'sgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sgo.wsgi.application'


# Banco de dados
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Recomendado no Linux/Ubuntu: definir credenciais por variáveis de ambiente.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_sgo',
        'USER': 'pi_1_26_user',
        'PASSWORD': 'Pi@1_2026',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Para SQLite (desenvolvimento sem MySQL):
#   export DJANGO_SETTINGS_MODULE=sgo.settings_sqlite
# Ou comente o bloco acima e descomente o SQLite abaixo.

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Validação de senha
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Idioma e fuso horário (Brasil)
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos (CSS, JavaScript, imagens)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Tipo padrão de chave primária
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'  # Para onde o usuário vai após logar
LOGOUT_REDIRECT_URL = 'login' # Para onde vai após deslogar
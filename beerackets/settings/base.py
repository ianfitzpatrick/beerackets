import json
from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured


def get_secret(secret_name):
    """
    Get secret variable or return explicit exception.

    Always return as string, not unicode.

    Must store this in base settings file due to structure of multiple
    settings files, or risk circular imports.
    """
    # Secrets file location
    cwd = os.path.dirname(os.path.realpath(__file__))
    project_dir = str(Path(cwd).parent)
    secrets_file = f'{project_dir}/settings/secrets.json'

    with open(secrets_file) as f:
        secrets_file = json.loads(f.read())
    try:
        return str(secrets_file[secret_name])

    except KeyError:
        error_msg = 'Missing secrets file.'
        raise Exception(error_msg)


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
TEMPLATE_DIR = str(Path(BASE_DIR).parents[1]) + '/templates'

SECRET_KEY = get_secret('SECRET_KEY')
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites.apps.SitesConfig',
    'django.contrib.humanize.apps.HumanizeConfig',
    'beerackets',
    'leagues',
    'teams',
    'matches',
    'ladders',
    'django_extensions'
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

ROOT_URLCONF = 'beerackets.urls'

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

WSGI_APPLICATION = 'beerackets.wsgi.application'

SITE_ID = 1

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'beerackets',
        'USER': 'beerackets',
        'PASSWORD': get_secret('DB_PASSWORD'),  # noqa: F405
        'HOST': '127.0.0.1',
        'OPTIONS': {
                'init_command': 'SET storage_engine=INNODB'
        }
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# DJango Wiki Settings
WIKI_MARKDOWN_HTML_STYLES = [
    'width', 'height', 'size', 'padding', 'margin', 'border', 'float',
    'display', 'max-width', 'min-width'
]

WIKI_MARKDOWN_HTML_WHITELIST = ['iframe']

WIKI_MARKDOWN_HTML_ATTRIBUTES = {
    'iframe': ['width', 'height', 'src']
}

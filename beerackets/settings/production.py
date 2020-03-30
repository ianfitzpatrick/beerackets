from .base import *  # noqa: F403
DEBUG = True
ALLOWED_HOSTS = [
    'winston.kqbdiscord.com'
]

DEBUG = True

SITE_ID = 2


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

SECURE_SSL_REDIRECT = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'beerackets',
        'USER': 'beerackets',
        'PASSWORD': get_secret('DB_PASSWORD'),  # noqa: F405
        'HOST': '',
        'OPTIONS': {
                'init_command': 'SET storage_engine=INNODB'
        }
    }
}

STATIC_ROOT = '/home/ianfitzpatrick/apps/beerackets_static'
MEDIA_ROOT = '/home/ianfitzpatrick/apps/beerackets_media'

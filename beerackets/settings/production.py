from .base import *  # noqa: F403

ALLOWED_HOSTS = [
    'winston.kqbdiscord.com'
]

DEBUG = False


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
STATICFILES_DIRS = '/home/ianfitzpatrick/apps/beerackets_static'
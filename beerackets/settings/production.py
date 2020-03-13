from .base import *  # noqa: F403

ALLOWED_HOSTS = [
    'beerackets.kqbdiscord.com'
]

DEBUG = False


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

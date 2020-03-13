from .base import *  

ALLOWED_HOSTS = ['*']
DEBUG = True
INTERNAL_IPS = ('127.0.0.1', '192.168.56.2', '192.168.56.1', '192.168.56.2')

STATIC_ROOT = '/var/www/beerackets_static/'
MEDIA_ROOT = '/var/www/beerackets_media/'
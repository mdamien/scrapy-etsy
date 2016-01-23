from .generic_settings import *

INSTALLED_APPS += [
    'etsy',
    'debug_toolbar',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'etsy',                      
        'USER': 'postgres',
        'PASSWORD': '',
    }
}
from .generic_settings import *

INSTALLED_APPS += [
    'etsy',
    #'debug_toolbar',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'etsy',                      
        'USER': 'postgres',
        'PASSWORD': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "collected_static/")

try:
    from .local_settings import *
except Exception as e:
    print('no local settings', e)
    pass

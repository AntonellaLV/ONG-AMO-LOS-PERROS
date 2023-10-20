from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Your Name DB',
        'USER': 'Your user',
        'PASSWORD': 'Your password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

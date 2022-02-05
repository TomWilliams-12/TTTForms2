from .base import *

SECRET_KEY = 'django-insecure-#f=@yl29ey9hv2!$m438rj#*z^nzmr0%*qck=_^$y^ss(db$ab'

DEBUG = int(os.environ.get('DEBUG', default=1))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tttforms',
    }
}

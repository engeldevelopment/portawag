import dj_database_url
from decouple import config

from .base import *


ALLOWED_HOSTS = [
	'127.0.0.1',
	'myportafoly.herokuapp.com'
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

DATABASES = {
	'default': dj_database_url.config(
		default=config('DATABASE_URL')
	)
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
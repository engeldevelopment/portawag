import dj_database_url
from decouple import config

from .base import *


ALLOWED_HOSTS = [
	'127.0.0.1',
	'localhost',
	'myportafoly.herokuapp.com'
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

DATABASES = {
	'default': dj_database_url.config(
		default=config('DATABASE_URL')
	)
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = [
	'compressor.filters.css_default.CssAbsoluteFilter',
	'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# -*- coding: utf-8 -*-
# Copyright (C) 2012 Rosen Diankov <rosen.diankov@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
IPYTHON_DEBUG = False
DEBUG = False
TEMPLATE_DEBUG = False

EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = SECRETS.get('email')
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_SUBJECT_PREFIX='[openrave.org] '
EMAIL_USE_TLS=True
SEND_BROKEN_LINK_EMAILS=True
SERVER_EMAIL='openrave.testing@gmail.com'
DEFAULT_FROM_EMAIL = 'openrave.testing@gmail.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'openrave_website',
        'USER': 'openrave',
        'PASSWORD': SECRETS['dbpass'],
        'HOST': 'openrave.org',
        'PORT': '5432',
        'TIME_ZONE': 'UTC',
    }
}

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = False
SECURE_FRAME_DENY = True
SECURE_HSTS_SECONDS = 600
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "SSL")

CACHES = {
    'default' : { 'BACKEND':'memcached://127.0.0.1:11011/',
#                   'LOCATION': '/var/tmp/django_cache',
#                   'TIMEOUT': 60,
#                   'OPTIONS': { 'MAX_ENTRIES': 1000 }
                }
}


CACHE_MIDDLEWARE_SECONDS = 60 * 5 # 5 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'openravedocs'
CACHE_MIDDLEWARE_GZIP = True
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

MIDDLEWARE_CLASSES.insert(0, 'django.middleware.cache.UpdateCacheMiddleware')
MIDDLEWARE_CLASSES.append('django.middleware.cache.FetchFromCacheMiddleware')

LOGGING["handlers"]["logfile"] = {
    "formatter": "full",
    "level": "DEBUG",
    "class": "logging.handlers.TimedRotatingFileHandler",
    "filename": "/var/log/openrave_website/website.log",
    "when": "D",
    "interval": 7,
    "backupCount": 5,
}
LOGGING["loggers"]["django.request"]["handlers"].append("logfile")
LOGGING["loggers"]["openrave_website"]["handlers"] = ["logfile"]

# necessary?
#HAYSTACK_SEARCH_ENGINE = 'xapian'
#HAYSTACK_XAPIAN_PATH = os.path.join(OPENRAVE_DOCUMENT_ROOT_PATH,'openravedocs.index')
    
#PUSH_SSL_CALLBACK = True

OPENRAVE_DOCUMENT_ROOT_PATH = '/var/openrave/docdata/'
MEDIA_ROOT = '/var/openrave/media/'
MEDIA_URL = '/m/'
STATICFILES_DIRS = ('/var/www/static/',)

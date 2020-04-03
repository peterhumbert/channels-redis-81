from .settings import *
import os

ALLOWED_HOSTS = ['repro-81-dev-async.us-west-2.elasticbeanstalk.com']

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(os.getenv('REDIS_HOST'), 6379)],
        },
    },
}

STATICFILES_DIRS = []
STATIC_ROOT = os.path.join(BASE_DIR, "static")

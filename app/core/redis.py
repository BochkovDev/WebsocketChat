import aioredis

from .settings import settings


redis = aioredis.from_url(settings.REDIS.URL, decode_responses=True)
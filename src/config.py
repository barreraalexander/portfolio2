from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str = 'd65f7ac9bffc5834652d88f8af72cac9581f88900c0a009733ba21ef7d1f22ac'
    debug: bool = True
    port: int = 4000

    # CACHE_DEFAULT_TIMEOUT = 180
    CACHE_DEFAULT_TIMEOUT = 0
    CACHE_TYPE: str = 'SimpleCache'

    # CACHE_TYPE = "RedisClusterCache"
    # CACHE_REDIS_CLUSTER = "titleleap-cache-redis-clustered.cmfdnq.clustercfg.use1.cache.amazonaws.com:6379"

settings = Settings()
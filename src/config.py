from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str = 'osmeke'
    debug: bool = True
    port: int = 4000
    cache_default_timeout: int = 180
    cache_type: str = 'SimpleCache'

settings = Settings()
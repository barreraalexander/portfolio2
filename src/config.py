from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str = 'osmeke'
    # debugging: bool = True
    debug: bool = True
    port: int = 4000
    # PORT: int = 4000

settings = Settings()
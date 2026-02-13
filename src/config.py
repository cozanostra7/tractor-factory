
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    DB_NAME:str
    DB_HOST: str
    DB_PORT: int
    DB_PASS: str
    DB_USER:str
    REDIS_HOST : str
    REDIS_PORT : int

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
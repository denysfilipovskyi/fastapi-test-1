import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = 'your-secret-key'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MONGO_URI: str = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
    DATABASE_NAME: str = 'users_crm'


settings = Settings()

import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'your-secret-key')
    ALGORITHM: str = os.getenv('ALGORITHM', 'HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv(
        'ACCESS_TOKEN_EXPIRE_MINUTES', 30)
    MONGO_URI: str = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
    DATABASE_NAME: str = os.getenv('DATABASE_NAME', 'users_crm')
    RABBIT_MQ_URL: str = os.getenv('RABBIT_MQ_URL', 'amqp://guest:guest@rabbitmq:5672/')


settings = Settings()

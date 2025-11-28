from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_TITLE: str = 'Community Blog and Mobile App Design'
    PROJECT_DESCRIPTION: str = 'A community-focused blog and mobile app design website'
    PROJECT_VERSION: str = '1.0.0'
    ALLOWED_ORIGINS: List[str] = ['http://localhost:3000']
    SQLALCHEMY_DATABASE_URL: str = 'sqlite:///./app.db'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SECRET_KEY: str = 'secret_key_here'
    ALGORITHM: str = 'HS256'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

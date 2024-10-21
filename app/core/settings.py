import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


APP_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = APP_DIR.parent

class DBSettings(BaseSettings):
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int

    @property
    def URL(self) -> str:
        return f'postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}'

    model_config = SettingsConfigDict(
        env_file=os.path.join(ROOT_DIR, '.env', '.env.db'),
        extra='ignore',
    )
_db = DBSettings()

class TemplateSettings(BaseSettings):
    TEMPLATE_DIR: Path = APP_DIR / 'templates'
    AUTO_RELOAD_TEMPLATES: bool

    model_config = SettingsConfigDict(
        env_file=os.path.join(ROOT_DIR, '.env', '.env.templates'),
        extra='ignore',
    )
_template = TemplateSettings()

class RedisSettings(BaseSettings):
    HOST: str
    PORT: int
    DATABASE: int = 0
    PASSWORD: str

    @property
    def URL(self) -> str:
        return f'redis://{self.HOST}:{self.PORT}/{self.DATABASE}'

    model_config = SettingsConfigDict(
        env_file=os.path.join(ROOT_DIR, '.env', '.env.redis'),
        extra='ignore',
    )
_redis = RedisSettings()

class AuthSettings(BaseSettings):
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=os.path.join(ROOT_DIR, '.env', '.env.auth'),
        extra='ignore',
    )
_auth = AuthSettings()

class Settings(BaseSettings):
    STATIC_DIR: Path = APP_DIR / 'static'
    SECRET_KEY: str
    DEBUG: bool
    DATABASE: DBSettings
    TEMPLATES: TemplateSettings
    REDIS: RedisSettings
    AUTH: AuthSettings
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(ROOT_DIR, '.env', '.env'),
        extra='ignore',
    )

settings = Settings(
    DATABASE=_db,
    TEMPLATES=_template,
    REDIS=_redis,
    AUTH=_auth,
)
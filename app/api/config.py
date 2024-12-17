import os
from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class __Settings(BaseSettings):
    """
    Application settings loaded from .env
    """
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', validate_assignment=True)


@lru_cache()
def get_settings():
    return __Settings()


settings = get_settings()
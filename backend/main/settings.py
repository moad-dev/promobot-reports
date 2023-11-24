from pydantic_settings import BaseSettings
from pydantic import (
    Field
)


class Settings(BaseSettings):
    frontend_url: str = Field(env="FRONTEND_URL")
    dummy_model: bool = Field(env="DUMMY_MODEL", default=True)

    class Config:
        env_file = '.env'


settings: Settings = Settings()

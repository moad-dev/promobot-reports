from pydantic_settings import BaseSettings
from pydantic import (
    AnyUrl,
    AnyHttpUrl,
    Field,
)


class Settings(BaseSettings):
    frontend_url: str = Field(..., env="FRONTEND_URL")

    class Config:
        env_file = '.env'


settings: Settings = Settings()
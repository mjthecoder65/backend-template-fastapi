from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """Settings for the application."""

    APP_NAME: str = Field(default="Backedend API Template")
    API_ROUTE_PREFIX: str = Field(default="/api/v1")
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=True
    )


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Ayvora API"
    environment: str = "production"

    database_url: str

    redis_url: str = "redis://redis:6379/0"

    jwt_secret: str = "change-me-in-production"

    allowed_origins: list[str] = [
        "http://localhost:3000"
    ]

    model_config = SettingsConfigDict(
        env_prefix="AYVORA_",
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Ayvora API"
    environment: str = "production"

    # Если готовый URL указан — используем его
    database_url: str | None = None

    # Иначе собираем из отдельных переменных
    sql_user: str = ""
    sql_password: str = ""
    sql_db_name: str = ""
    sql_host: str = ""

    redis_url: str = "redis://redis:6379/0"

    jwt_secret: str = "change-me-in-production"

    allowed_origins: list[str] = [
        "http://localhost:3000"
    ]

    model_config = SettingsConfigDict(
        env_prefix="AYVORA_",
        env_file=".env",
        extra="ignore",
    )

    @property
    def database_uri(self) -> str:
        if self.database_url:
            return self.database_url

        password = quote_plus(self.sql_password)

        return (
            f"postgresql+psycopg://"
            f"{self.sql_user}:{password}"
            f"@/{self.sql_db_name}"
            f"?host={self.sql_host}"
        )


settings = Settings()

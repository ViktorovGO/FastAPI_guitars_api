from typing import Literal
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pydantic import Field, ConfigDict

load_dotenv()

LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


class db_settings(BaseSettings):
    DB_USER: str = Field("postgres", json_schema_extra=({"env": "DB_USER"}))
    DB_PASS: str = Field("postgres", json_schema_extra=({"env": "DB_PASS"}))
    DB_NAME: str = Field("postgres", json_schema_extra=({"env": "DB_NAME"}))
    DB_HOST: str = Field("127.0.0.1", json_schema_extra=({"env": "DB_HOST"}))
    DB_PORT: int = Field(5433, json_schema_extra=({"env": "DB_PORT"}))
    db_echo: bool = True

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


class Run(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8001


class GunicornConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    timeout: int = 900


class LoggingConfig(BaseSettings):
    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    log_format: str = LOG_DEFAULT_FORMAT


class Settings(BaseSettings):
    db: db_settings = db_settings()
    run: Run = Run()
    gunicorn: GunicornConfig = GunicornConfig()
    logging: LoggingConfig = LoggingConfig()

    model_config = ConfigDict(env_file="../../.env")


settings = Settings()

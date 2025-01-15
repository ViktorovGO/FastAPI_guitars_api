from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict
from dotenv import load_dotenv
import os

load_dotenv()

class db_settings(BaseSettings):
    DB_USER: str = Field('postgres', json_schema_extra=({"env":"DB_USER"}))
    DB_PASS: str = Field('postgres', json_schema_extra=({"env":"DB_PASS"}))
    DB_NAME: str = Field('postgres', json_schema_extra=({"env":"DB_NAME"}))
    DB_HOST: str = Field('127.0.0.1', json_schema_extra=({"env":"DB_HOST"}))
    DB_PORT: int = Field(5433, json_schema_extra=({"env":"DB_PORT"}))
    db_echo: bool = True
    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST\
        }:{self.DB_PORT}/{self.DB_NAME}"


class Settings(BaseSettings):
    db: db_settings = db_settings()
    model_config = ConfigDict(env_file="../../.env")


settings = Settings()


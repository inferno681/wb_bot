from pathlib import Path

import yaml
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseModel):
    """Redis settings."""

    host: str
    port: int
    redis_db: int


class APISettings(BaseModel):

    base_url: str


class Secrets(BaseSettings):
    """Secrets settings."""

    token: SecretStr = SecretStr('token')

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )


class AppConfig(BaseSettings):
    """Main configuration class."""

    redis: RedisSettings
    api: APISettings
    secrets: Secrets

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='allow',
    )

    @classmethod
    def load_settings(cls, file_path: str) -> 'AppConfig':
        """Load configuration from YAML and environment variables."""
        yaml_config = yaml.safe_load(
            Path(file_path).read_text(encoding='utf-8')
        )
        return cls(**yaml_config, secrets=Secrets())


config = AppConfig.load_settings('src/config/config.yaml')

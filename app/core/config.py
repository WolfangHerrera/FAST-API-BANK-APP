from pydantic_settings import BaseSettings
from pydantic.fields import Field


class Settings(BaseSettings):
    mongo_uri: str = Field(..., env="MONGO_URI")

    class Config:
        env_file = ".env"
        extra = "forbid"


settings = Settings()

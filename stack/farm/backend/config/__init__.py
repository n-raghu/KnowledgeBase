from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Intro"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 369


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb://root:mangodb@172.99.16.5/admin?retryWrites=true&w=majority"
    DB_NAME: str = "farmstack"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()

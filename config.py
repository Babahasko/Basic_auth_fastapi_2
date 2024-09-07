from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
from pydantic import BaseModel

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8001

class ApiPrefix(BaseModel):
    prefix: str = "/api"

class DatabaseConfig(BaseModel):
    url: PostgresDsn

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig

settings = Settings()


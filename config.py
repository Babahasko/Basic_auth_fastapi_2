from pydantic_settings import BaseSettings
from pydantic import BaseModel

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8001

class ApiPrefix(BaseModel):
    prefix: str = "/api"

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

settings = Settings()


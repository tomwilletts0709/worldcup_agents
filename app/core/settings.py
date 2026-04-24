from pydantic import BaseSettings
from pydantic import PostgresDsn

class Settings(BaseSettings): 
    app_name: str = "Langchain App to mess around with LLMS"
    OPEN_API_KEY: str 
    ANTHROPIC_API_KEY: str

class Config(BaseSettings): 
    DATABASE_URL: PostgresDsn

    CORS_ORIGINS: list[str]
    COR

settings = Settings()


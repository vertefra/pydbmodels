import os

class Settings:
    database_url: str | None  
    database: str = 'postgres'
    location: str = "_models"

def init_settings() -> Settings:
    database_url = os.getenv('DATABASE_URL')
    s = Settings()
    s.database_url = database_url

    return s

config = init_settings()
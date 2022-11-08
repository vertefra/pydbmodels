import os
from typing import TypedDict

class IdentifierSettings(TypedDict):
    column_identifier: str
    include_in_model: bool
    include_in_initializer: bool
    include_in_updater: bool



class Settings:
    database_url: str | None  
    database: str = 'postgres'
    location: str = "_models"
    identifier_settings: IdentifierSettings = {
        'column_identifier': 'id',
        'include_in_model': True,
        'include_in_initializer': False,
        'include_in_updater': True
    }

def init_settings() -> Settings:
    database_url = os.getenv('DATABASE_URL')
    s = Settings()
    s.database_url = database_url

    return s

config = init_settings()
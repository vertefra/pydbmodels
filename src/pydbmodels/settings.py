import os
from typing import TypedDict


class IdentifierSettings(TypedDict):
    column_identifier: str
    include_in_model: bool
    include_in_initializer: bool
    include_in_updater: bool


class Settings:
    database_url: str | None = None
    database: str = "postgres"
    generator: str = "pydantic"
    location: str = "_models"
    user_defined_file_name: str = "user_defined.py"
    table_template_file_name: str = "_table_templates.j2"
    user_defined_template_file_name = "_user_defined_templates.j2"
    schema_init_file_templates = "_schema_init_file_templates.j2"

    identifier_settings: IdentifierSettings = {
        "column_identifier": "id",
        "include_in_model": True,
        "include_in_initializer": False,
        "include_in_updater": True,
    }


def init_settings() -> Settings:
    database_url = os.getenv("DATABASE_URL")
    generator = os.getenv("GENERATOR")
    location = os.getenv("LOCATION")

    s = Settings()

    s.database_url = s.database_url or database_url
    s.generator = generator or s.generator
    s.location = location or s.location

    return s


config = init_settings()

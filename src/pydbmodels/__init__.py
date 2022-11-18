from dbmeta import dbmeta  # type: ignore
from dbmeta.connections.postgres import exclude  # type: ignore

from .settings import config
from .generators import InitGenerator
from .generators.templates.models import GenerateModels


def generate(db_type: str | None, db_url: str | None):
    if db_type:
        config.database = db_type

    if db_url:
        config.database_url = db_url

    metadata = dbmeta.gen_metadata(config.database, config.database_url)

    # For now, only option is pydantic

    generator = InitGenerator(config.generator)
    generator.build(metadata)

    tree = generator.tree
    user_defined = [ud for ud in generator.user_defined.values()]
    imports = generator.imports
    base_classes = generator.base_classes

    models = GenerateModels(
        tree,
        user_defined,
        imports,
        base_classes,
    )

    models.write()

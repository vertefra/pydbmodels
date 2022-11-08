from dbmeta import dbmeta
from dbmeta.connections import exclude

from .settings import config
from .generators.pydantic.generator import PydanticGenerator
from .generators.pydantic.templates.models import GenerateModels

def generate(db_type: str | None, db_url: str | None):
    if db_type:
        config.database = db_type

    if db_url:
        config.database_url = db_url

    metadata = dbmeta.gen_metadata(config.database, config.database_url)
    p = PydanticGenerator()
    tree = p.build(metadata)
    g = GenerateModels(tree, [{"from": "pydantic", "import": "BaseModel"}, {"from": "typing", "import": "Union"}], ['BaseModel'])
    g.write()
    
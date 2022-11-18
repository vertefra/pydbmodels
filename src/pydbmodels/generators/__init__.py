from .generator import IGenerator
from .pydantic.generator import PydanticGenerator


def InitGenerator(gen_type: str) -> IGenerator:
    if gen_type == "pydantic":
        return PydanticGenerator()

    raise Exception(f"Generator {gen_type} not implemented")

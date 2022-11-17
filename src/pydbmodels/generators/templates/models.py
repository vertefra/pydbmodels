from ..generator import Tree, GenType
from ..generator import TableFile
from ...settings import config
from typing import Dict, Any, List, Set, Tuple
from jinja2 import Environment, Template
import os
import black
from black.mode import Mode

env = Environment(autoescape=False, optimized=False)


def unpack_import(import_dict: Dict[str, str]) -> Tuple[str, str | None]:
    """ Takes a python dictionary with keys "import" and "from" and returns a tuple with the values 
        Makes sure the keys are present and that the "import" key is not empty
    """
    import_: str = ""
    from_: str | None = None

    if "import" not in import_dict:
        raise KeyError(f"Malformed import dictionary. {import_dict}")

    import_ = import_dict["import"]

    if "from" not in import_dict or import_dict["from"] is None:
        from_ = None
    else:
        from_ = import_dict["from"]

    return import_, from_


def folder() -> str:
    module = __file__
    split = module.split("/")[:-1]
    return "/".join(split)

class _FromImportHeader:
    imports: Dict[str, Set[str]] # key is the module and the set is the imports

    def __init__(self) -> None:
        self.imports = {}

    def add_import(self, module: str, import_: str) -> None:
        if module not in self.imports:
            self.imports[module] = set()

        self.imports[module].add(import_)


class _ImportHeader:
    imports: Set[str]

    def __init__(self) -> None:
        self.imports = set()

    def add_import(self, import_: str) -> None:
        self.imports.add(import_)


class GenerateModels:
    models_folder: str
    tree: Tree
    generator_imports: List[Dict[str, str]]

    def __init__(
        self,
        tree: Tree,
        generator_imports: List[Dict[str, str]] = [],
        class_parents: List[str] = [],
    ) -> None:
        self.models_folder = config.location
        self.tree = tree
        self.generator_imports = generator_imports
        self.class_parents = class_parents

    def write(self) -> None:
        for schema in self.tree:
            table_file = self.tree[schema]
            self.write_table(schema, table_file)

    def write_table(self, schema: str, tables: TableFile):

        for table_name in tables:
            table_types = tables[table_name]

            file_path = f"{self.models_folder}/{schema}/{table_name}.py"

            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            imports = self.__consolidating_imports(table_types)

            from_import_header: Dict[str, Set[str]] = imports["from_import_header"]
            import_header: Set[str] = imports["import_header"]

            with open(file_path, "w") as write_file:
                with open(f"{folder()}/_table_templates.j2", "r") as template_file:
                    t = env.from_string(template_file.read())
                    t.stream(
                        from_imports=from_import_header,
                        import_header=import_header,
                        table_name=self.__pretty_table_name(table_name),
                        table_types=table_types,
                        class_parents=self.class_parents,
                        identifier=config.identifier_settings,
                    ).dump(write_file)

            black.format_file_contents(file_path, fast=False, mode=Mode())

    def __pretty_table_name(self, name: str) -> str:
        split = name.split("_")
        capitalized = [n.capitalize() for n in split]
        return "".join(capitalized)

    # This also adds the specific generator imports and other based on the genTypes
    def __consolidating_imports(self, gen_types: List[GenType]) -> Dict[str, Any]:
        # from ... import ... statements
        from_import_header = _FromImportHeader()
        
        # import ... statements
        import_header = _ImportHeader()

        # Adding specific generator imports if present
        for import_dict in self.generator_imports:
            import_, from_ = unpack_import(import_dict)

            # If from_ is defined, the is a from... import statement
            if from_:
                from_import_header.add_import(from_, import_)
            else:
                import_header.add_import(import_)

        # Adding model imports
        for model in gen_types:
            if model.is_union:
                # Add from typing import Union
                from_import_header.add_import("typing", "Union")

            if model.nullable:
                # Add from typing import Optional
                from_import_header.add_import("typing", "Union")

            if model.imports:
                for import_dict in model.imports:
                    model_import, model_from = unpack_import(import_dict)

                    if model_from:
                        from_import_header.add_import(model_from, model_import)
                    else:
                        import_header.add_import(model_import)

        return {
            "from_import_header": from_import_header.imports,
            "import_header": import_header.imports,
        }

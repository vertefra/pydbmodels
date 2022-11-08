from ..generator import Tree, GenType
from ...generator import TableFile
from ....settings import config
from typing import Dict, Any, List, Set
from jinja2 import Environment, Template
import os

env = Environment(autoescape=False, optimized=False)

def folder() -> str:
    module = __file__
    split = module.split('/')[:-1]
    return "/".join(split)


class GenerateModels:
    models_folder: str
    tree: Tree
    generator_imports: List[Dict[str, str]] 

    def __init__(self, tree: Tree, generator_imports: List[Dict[str, str]] = [], class_parents: List[str] = []) -> None:
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
            
            from_import_header: Dict[str, Set[str]] = imports['from_import_header']
            import_header: Set[str] = imports['import_header']

            with open(file_path, "w") as write_file:
                with open(f'{folder()}/_table_templates.j2', "r") as template_file:
                    t = env.from_string(template_file.read())
                    t.stream(
                        from_imports=from_import_header,
                        import_header=import_header,
                        table_name=self.__pretty_table_name(table_name),
                        table_types=table_types,
                        class_parents=self.class_parents
                    ).dump(write_file)  
    
    def __pretty_table_name(self, name: str) -> str:
        split = name.split('_')
        capitalized = [n.capitalize() for n in split]
        return "".join(capitalized)

    # This also adds the specific generator imports and other based on the genTypes
    def __consolidating_imports(self, gen_types: List[GenType]) -> Dict[str, Any]:
        from_import_header: Dict[str, Set[str]] = {}
        import_header: Set[str] = set()

        # Adding specific generator imports if present
        for import_dict in self.generator_imports:
            from_ = import_dict.get('from')
            import_: str = import_dict.get('import')

            if from_:
                # from ... import statement

                current_imports = from_import_header.get(from_, set())
                current_imports.add(import_)
                from_import_header[from_] = current_imports

            else:
                # import ... statement
                        import_header.add(import_)

        # Adding model imports
        for model in gen_types:
            print(f"{model.name} - {model.is_union}")
            
            if model.is_union:
                # Add from typing import Union
                current_imports = from_import_header.get('typing', set())
                current_imports.add('Union')
                from_import_header["typing"] = current_imports

            if model.nullable:
                current_imports = from_import_header.get('typing', set())
                current_imports.add('Union')
                from_import_header["typing"] = current_imports
            
            if model.imports:
                for import_dict in model.imports:
                    from_ = import_dict.get('from')
                    import_: str = import_dict.get('import')

                    if from_:
                        # from ... import statement

                        current_imports = from_import_header.get(from_, set())
                        current_imports.add(import_)
                        from_import_header[from_] = current_imports

                    else:
                        # import ... statement
                        import_header.add(import_)

        return {
            "from_import_header": from_import_header,
            "import_header": import_header
        }

    

            
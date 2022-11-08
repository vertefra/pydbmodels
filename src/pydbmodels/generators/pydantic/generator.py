from typing import List
from .type_map import type_map
from ..generator import GenType, Tree, IColumn, IMetadata, IGenerator
import re

class PydanticGenerator(IGenerator):
    # Define the imports at the beginning of the generated file
    class_imports: List[str]
    # Define the base classes that the model should inherit from
    class_parents: List[str]
    # folders with schema names
    tree: Tree 

    def build(self, metadata: IMetadata) -> Tree:
        
        self.tree = {}

        for schema in metadata.schema:
            self.tree[schema.schema_name] = {}
            
            for table in schema.tables:

                table_name = table.table_name
                self.tree[schema.schema_name][table_name] = []
                
                for column in table.columns:
                    g_type = self.build_gen_type(column)
                    self.tree[schema.schema_name][table_name].append(g_type)

        return self.tree

    def build_gen_type(self, column: IColumn) -> GenType:
        g = GenType()
        g.name = column.column_name
        g.nullable = True if column.is_nullable == 'YES' else False
        
        # Gets the python mapping for the database type
        name_type = column.udt_name
        val_type = type_map.get_type(name_type)

        if val_type is None:
            raise Exception(f'No type found for {name_type}')

        g.imports = val_type.imports
        g.str_value = val_type.str_value
        
        g.has_default = column.column_default is not None and column.column_default != ''
        g.is_union = len(g.str_value) > 1

        if g.is_union:
            g.imports.append({"from": "typing", "import": "Union"})

        return g

    def _is_function(self, pg_default: str) -> bool:
        fn_pattern = '^[A-Za-z0-9_-]*\([A-Za-z0-9\':_]*?\)$'

        return re.search(fn_pattern, pg_default) != None
        
    def _is_array(self, pg_default: str) -> bool:
        return pg_default.startswith('ARRAY[') and pg_default.endswith("]")

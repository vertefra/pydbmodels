from typing import List, Dict

from .type_map import type_map, NameType
from ..generator import (
    GenType,
    Tree,
    IColumn,
    IMetadata,
    IGenerator,
    IUserDefined,
    FolderName,
    TableName,
    IUserDefinedRaw,
    ISchema,
)
import re


class UserDefined(IUserDefined):
    name: str
    class_name: str  # How it will be represented in the model
    is_enum: bool = True  # For now we only support enums
    elements: List[str]

    def __init__(self, name: str, elements: List[str]) -> None:
        self.name = name
        self.elements = elements
        self.class_name = self._get_class_name(name)

    def _get_class_name(self, name: str) -> str:
        """Converts the name of the type to a valid class name"""
        name = name.replace("_", " ")
        name = name.title()
        name = name.replace(" ", "")
        return name

    def __repr__(self) -> str:
        return f"{self.__dict__}"


def convert_raw_user_defined(
    user_defined: List[IUserDefinedRaw[str]],
) -> List[IUserDefined]:
    """Elements are saved in the `elements` field as \n separated strings."""
    user_defined_parsed: List[IUserDefined] = []

    for ud in user_defined:
        elements = ud.elements.split("\n")
        elements = [e.strip() for e in elements]
        elements = [e for e in elements if e != ""]

        user_defined_parsed.append(UserDefined(name=ud.name, elements=elements))

    return user_defined_parsed


class PydanticGenerator(IGenerator):
    # Define the imports at the beginning of the generated file
    class_imports: List[str]
    # Define the base classes that the model should inherit from
    class_parents: List[str]
    # folders with schema names
    _tree: Tree = {}
    # user defined types
    _user_defined: Dict[str, IUserDefined] = {}
    # generator specific imports
    _imports: List[Dict[str, str]] = [
        {"from": "pydantic", "import": "BaseModel"},
        {"from": "typing", "import": "Union"},
    ]
    # generator specific base classes
    _base_classes: List[str] = ["BaseModel"]

    # Property to satisfy IGenerator interface
    @property
    def base_classes(self) -> List[str]:
        return self._base_classes

    @property
    def imports(self) -> List[Dict[str, str]]:
        return self._imports

    @property
    def tree(self) -> Tree:
        return self._tree

    @property
    def user_defined(self) -> Dict[str, IUserDefined]:
        return self._user_defined

    # Public method to build all the folder structure with models
    def build(self, metadata: IMetadata[str]) -> None:
        """Build the folder tree and the user defined types."""
        self._user_defined = self.__build_user_defined(metadata.user_defined)
        self._tree = self.__build_folder_tree(metadata.schema)

    # Private method to build all the folder tree
    def __build_folder_tree(self, _schema: List[ISchema]) -> Tree:
        tree: Tree = {}

        for schema in _schema:
            folder_name = FolderName(schema.schema_name)
            tree[folder_name] = {}

            for table in schema.tables:

                table_name = TableName(table.table_name)
                tree[folder_name][table_name] = []

                for column in table.columns:
                    g_type = self.build_gen_type(column)
                    tree[folder_name][table_name].append(g_type)

        return tree

    # Private method to build all the user defined types
    def __build_user_defined(
        self, user_defined: List[IUserDefinedRaw[str]]
    ) -> Dict[str, IUserDefined]:
        _user_defined = convert_raw_user_defined(user_defined)
        return {ud.name: ud for ud in _user_defined}

    def build_gen_type(self, column: IColumn) -> GenType:
        g = GenType()
        g.name = column.column_name
        g.nullable = True if column.is_nullable == "YES" else False

        # Gets the python mapping for the database type
        name_type = NameType(column.udt_name)
        val_type = type_map.get_type(name_type)

        if val_type is None:
            # Check if the type is user defined
            if name_type in self.user_defined:
                ud = self.user_defined[name_type]
                g.str_value = [ud.class_name]
                g.imports = [{"from": "..user_defined", "import": ud.class_name}]
            else:
                raise Exception(f"No type found for {name_type}")
        else:
            g.imports = val_type.imports or []
            g.str_value = val_type.str_value

        g.has_default = (
            column.column_default is not None and column.column_default != ""
        )
        g.is_union = len(g.str_value) > 1

        if g.is_union or g.nullable:
            g.imports.append({"from": "typing", "import": "Union"})

        return g

    def _is_function(self, pg_default: str) -> bool:
        fn_pattern = "^[A-Za-z0-9_-]*\([A-Za-z0-9':_]*?\)$"

        return re.search(fn_pattern, pg_default) != None

    def _is_array(self, pg_default: str) -> bool:
        return pg_default.startswith("ARRAY[") and pg_default.endswith("]")

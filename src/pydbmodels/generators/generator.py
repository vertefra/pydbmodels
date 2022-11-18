from typing import List, NewType, Dict, Any, Protocol, TypeVar, Generic
from abc import ABC, abstractmethod


class GenType:
    """Class that describes the type on a column in a way that is interpretable by GenerateModels class"""

    name: str
    str_value: List[str]
    imports: List[
        Dict[str, str]
    ] | None = None  # list of dictionaries { "from": str | None, "import": str}
    nullable: bool
    has_default: bool = False
    is_union: bool = False

    def __repr__(self) -> str:
        return f"<{self.name} :: {self.str_value} :: is nullable: {self.nullable} :: imports {self.imports}>"


ModelName = NewType("ModelName", str)
FolderName = NewType("FolderName", str)
TableName = NewType("TableName", str)

TableFile = Dict[TableName, List[GenType]]
Tree = Dict[FolderName, TableFile]

# Types used will be the one from dbmeta, but
# placing them behind these interfaces


class IColumn(Protocol):
    column_name: str
    is_nullable: str
    udt_name: str
    column_default: str


class ITable(Protocol):
    table_name: str
    columns: List[IColumn]


class ISchema(Protocol):
    schema_name: str
    tables: List[ITable]


ElementType = TypeVar("ElementType")


class IUserDefinedRaw(Generic[ElementType], Protocol):
    """Interface for user defined types before parsing the different elements"""

    name: str
    elements: ElementType  # Postgres generator returns a string as ElementType, where all the elements are divided by \n


class IUserDefined(Protocol):
    name: str  # How the user defined is represented as a datatype in the database
    elements: List[str]  # List of elements that the user defined type contains
    is_enum: bool  # True if the user defined type is an enum
    class_name: str  # Name of the class that will be generated for the user defined type


class IMetadata(Generic[ElementType], Protocol):
    schema: List[ISchema]
    user_defined: List[IUserDefinedRaw[ElementType]]


class IGenerator(ABC):
    """Interface that implements the build method to create the folders tree"""

    @property
    @abstractmethod
    def imports(self) -> List[Dict[str, str]]:
        """Default import for the generated models
        List of dictionaries in the format { "from": str | None, "import": str}
        """
        ...

    @property
    @abstractmethod
    def base_classes(self) -> List[str]:
        """Default base classes for the generated models"""
        ...

    @property
    @abstractmethod
    def tree(self) -> Tree:
        ...

    @property
    @abstractmethod
    def user_defined(self) -> Dict[str, IUserDefined]:
        ...

    @abstractmethod
    def build(self, metadata: IMetadata) -> None:
        ...

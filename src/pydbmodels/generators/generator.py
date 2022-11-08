from typing import List, NewType, Dict, Protocol
from abc import ABC, abstractmethod

class GenType:
    name: str
    str_value: List[str]
    imports: List[Dict[str, str]] | None = None # list of dictionaries { "from": str | None, "import": str}
    nullable: bool
    has_default: bool = False
    is_union: bool = False

    def __repr__(self) -> str:
        return f"<{self.name} :: {self.str_value} :: is nullable: {self.nullable} :: imports {self.imports}>"


ModelName = NewType('ModelName', str)
FolderName = NewType('FolderName', str)

TableName = NewType('TableName', str)
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

class IMetadata(Protocol):
      schema: List[ISchema]

class IGenerator(ABC):
    """ Interface that implements the build method to create the folders tree """

    @abstractmethod
    def build(self, metadata: IMetadata) -> Tree:
        pass
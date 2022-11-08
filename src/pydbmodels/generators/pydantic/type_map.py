from typing import NewType, Dict, Tuple
from ..types import ValType, TText, TInt, TDatetime, TJson, TBool
from typing import List

NameType = NewType("NameType", str)

# Typing imports for some common types
list_import: List[Dict[str, str]] = [{"from": "typing", "import": "List"}]


def generate_list_valType(name: NameType, val: ValType) -> Tuple[NameType, ValType]:
    v = ValType()

    imports = [*(val.imports or []), *(list_import or [])]
    
    # _ it's how postgres indicates array type

    pg_type: NameType = f"_{name}"
    val = f"List[{', '.join(val.str_value)}]"
    v.imports = imports
    v.str_value = [val]
    
    return pg_type,  v


class type_map:
    _type_map: Dict[NameType, ValType] = {}

    @classmethod
    def register_type(cls, name: NameType, val: ValType) -> None:
        # Register type
        cls._type_map[name] = val
        # Register array
        array_name, array_val_type = generate_list_valType(name, val)
        cls._type_map[array_name] = array_val_type


    @classmethod
    def get_type(cls, name: NameType) -> ValType | None:
        return cls._type_map.get(name)


type_map.register_type("text", TText)
type_map.register_type("int8", TInt)
type_map.register_type("int4", TInt)
type_map.register_type("timestamptz", TDatetime)
type_map.register_type("timestamp", TDatetime)
type_map.register_type("json", TJson)
type_map.register_type("jsonb", TJson)
type_map.register_type("uuid", TText)
type_map.register_type("varchar", TText)
type_map.register_type("bool", TBool)
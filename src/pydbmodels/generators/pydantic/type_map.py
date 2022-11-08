from typing import NewType, Dict, Tuple
from ..types import ValType, TText, TInt, TDatetime, TJson, TBool
from typing import List

NameType = NewType("NameType", str)

# Typing imports for some common types
list_import: List[Dict[str, str]] = [{"from": "typing", "import": "List"}]


def generate_list_valType(name: NameType, val: ValType) -> Tuple[NameType, ValType]:
    v = ValType()

    imports = [*(val.imports or []), *(list_import or [])]
    v.imports = imports

    # _ it's how postgres indicates array type

    pg_type: NameType = f"_{name}"

    # if only one type of value is present generate a `List[<type]`
    # otherwise a union of lists

    if len(val.str_value) == 1:
        v.str_value = [f'List[{val.str_value[0]}]']
        v.imports.append({"from": "typing", "import": "List"})
    elif len(val.str_value) > 1:
        _union = ''

        for value in val.str_value:
            if len(_union) < 1:
                _union = f"List[{value}]"
            else:
                _union = f"{_union}, List[{value}]"

        v.str_value = [f'Union[{_union}]']
        v.imports.extend([{"from": "typing", "import": "List"}, {"from": "typing", "import": "Union"}])
    
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
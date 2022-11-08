from typing import List, Dict

class ValType:
    # representation of the possible types
    str_value: List[str]
    imports: List[Dict[str, str]] | None = None


class TText(ValType):
    str_value = ['str']

class TInt(ValType):
    str_value: str = ['int']

class TDatetime(ValType):
    str_value: str = ['datetime']
    imports = [{"from": "datetime", "import": "datetime"}]

class TJson(ValType):
    str_value: str = ['Dict[str, Any]', 'str']
    imports = [{"from": "typing", "import": "Dict"}, {"from": "typing", "import": "Any"}]

class TBool(ValType):
    str_value: List[str] = ["bool"]
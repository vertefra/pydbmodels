from src.pydbmodels.generators.pydantic.type_map import type_map
from src.pydbmodels.generators.types import ValType, TText
from src import generate


class TAuthService(ValType):
    str_value = ["str"]

class TUserRole(ValType):
    str_value = ["str"]

class TGroupType(ValType):
    str_value = ["str"]

class TSharingLevel(ValType):
    str_value = ["str"]

class TdSessionType(ValType):
    str_value = ["str"]

class TProvider(ValType):
    str_value = ["str"]

class TSessionEvent(ValType):
    str_value = ["str"]

class TFriendshipStatus(ValType):
    str_value = ["str"]


type_map.register_type("auth_service_t", TAuthService)
type_map.register_type("user_role_t", TUserRole)
type_map.register_type("group_type_t", TGroupType)
type_map.register_type("sharing_level_t", TSharingLevel)
type_map.register_type("session_type_t", TdSessionType)
type_map.register_type("provider_t", TProvider)
type_map.register_type("session_event_type_t", TSessionEvent)
type_map.register_type("friendship_status_t", TFriendshipStatus)
type_map.register_type("int8", TText)

generate('postgres', 'postgres://postgres:postgres1@localhost:9876/postgres?sslmode=disable')
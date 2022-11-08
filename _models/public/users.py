from pydantic import BaseModel
from typing import Union, List
from datetime import datetime


class UsersModel(BaseModel):
    
    id: str
    auth_id: str
    auth_service: str
    first_name: Union[str, None]
    email: Union[str, None]
    phone_number: Union[str, None]
    created_at: datetime
    updated_at: datetime
    location: Union[str, None]
    google_place_id: Union[str, None]
    interest_ids: Union[List[int], None]
    timezone: Union[str, None]
    bio: Union[str, None]
    profile_image_url: Union[str, None]
    last_name: Union[str, None]
    registered_at: Union[datetime, None]
    deleted_at: Union[datetime, None]
    disabled_at: Union[datetime, None]
    last_login: datetime
    permission_id: Union[str, None]
    roles: Union[List[str], None]
    user_handle: Union[str, None]




class UsersInitializer(BaseModel):
    
    id: Union[str, None] = None
    auth_id: str
    auth_service: str
    first_name: str
    email: str
    phone_number: str
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    location: str
    google_place_id: str
    interest_ids: List[int]
    timezone: str
    bio: str
    profile_image_url: str
    last_name: str
    registered_at: datetime
    deleted_at: datetime
    disabled_at: datetime
    last_login: Union[datetime, None] = None
    permission_id: str
    roles: Union[List[str], None] = None
    user_handle: str




class UsersUpdater(BaseModel):
    id: Union[str, None] = None 
    auth_id: Union[str, None] = None 
    auth_service: Union[str, None] = None 
    first_name: Union[str, None] = None 
    email: Union[str, None] = None 
    phone_number: Union[str, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    location: Union[str, None] = None 
    google_place_id: Union[str, None] = None 
    interest_ids: Union[List[int], None] = None 
    timezone: Union[str, None] = None 
    bio: Union[str, None] = None 
    profile_image_url: Union[str, None] = None 
    last_name: Union[str, None] = None 
    registered_at: Union[datetime, None] = None 
    deleted_at: Union[datetime, None] = None 
    disabled_at: Union[datetime, None] = None 
    last_login: Union[datetime, None] = None 
    permission_id: Union[str, None] = None 
    roles: Union[List[str], None] = None 
    user_handle: Union[str, None] = None 
    
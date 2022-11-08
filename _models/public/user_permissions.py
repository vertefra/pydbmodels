from pydantic import BaseModel
from typing import Union
from datetime import datetime


class UserPermissionsModel(BaseModel):
    
    id: str
    allow_messaging: bool
    share_activities: Union[str, None]
    share_profile: Union[str, None]
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]




class UserPermissionsInitializer(BaseModel):
    
    id: Union[str, None] = None
    allow_messaging: Union[bool, None] = None
    share_activities: Union[str, None] = None
    share_profile: Union[str, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None




class UserPermissionsUpdater(BaseModel):
    id: Union[str, None] = None 
    allow_messaging: Union[bool, None] = None 
    share_activities: Union[str, None] = None 
    share_profile: Union[str, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    
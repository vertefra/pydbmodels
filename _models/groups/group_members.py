from pydantic import BaseModel
from typing import Union
from datetime import datetime


class GroupMembersModel(BaseModel):
    
    id: str
    user_id: str
    group_id: str
    permission_id: str
    canceled_at: Union[datetime, None]
    created_at: Union[datetime, None]




class GroupMembersInitializer(BaseModel):
    
    id: Union[str, None] = None
    user_id: str
    group_id: str
    permission_id: str
    canceled_at: datetime
    created_at: Union[datetime, None] = None




class GroupMembersUpdater(BaseModel):
    id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    group_id: Union[str, None] = None 
    permission_id: Union[str, None] = None 
    canceled_at: Union[datetime, None] = None 
    created_at: Union[datetime, None] = None 
    
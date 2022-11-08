from pydantic import BaseModel
from typing import Union
from datetime import datetime


class FriendshipsModel(BaseModel):
    
    id: str
    user_id: str
    other_user_id: str
    canceled_at: Union[datetime, None]
    created_at: datetime
    friendship_status: Union[str, None]
    permission_id: Union[str, None]




class FriendshipsInitializer(BaseModel):
    
    id: Union[str, None] = None
    user_id: str
    other_user_id: str
    canceled_at: datetime
    created_at: Union[datetime, None] = None
    friendship_status: str
    permission_id: str




class FriendshipsUpdater(BaseModel):
    id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    other_user_id: Union[str, None] = None 
    canceled_at: Union[datetime, None] = None 
    created_at: Union[datetime, None] = None 
    friendship_status: Union[str, None] = None 
    permission_id: Union[str, None] = None 
    
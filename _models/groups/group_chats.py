from pydantic import BaseModel
from typing import Union
from datetime import datetime


class GroupChatsModel(BaseModel):
    
    id: str
    group_id: str
    chat_id: str
    removed_at: Union[datetime, None]
    added_at: Union[datetime, None]




class GroupChatsInitializer(BaseModel):
    
    id: Union[str, None] = None
    group_id: str
    chat_id: str
    removed_at: datetime
    added_at: Union[datetime, None] = None




class GroupChatsUpdater(BaseModel):
    id: Union[str, None] = None 
    group_id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    removed_at: Union[datetime, None] = None 
    added_at: Union[datetime, None] = None 
    
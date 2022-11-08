from pydantic import BaseModel
from typing import Union
from datetime import datetime


class ChatMembersModel(BaseModel):
    
    id: str
    chat_id: str
    user_id: str
    canceled_at: Union[datetime, None]
    created_at: datetime
    updated_at: datetime




class ChatMembersInitializer(BaseModel):
    
    id: Union[str, None] = None
    chat_id: str
    user_id: str
    canceled_at: datetime
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None




class ChatMembersUpdater(BaseModel):
    id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    canceled_at: Union[datetime, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    
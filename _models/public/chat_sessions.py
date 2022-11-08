from pydantic import BaseModel
from typing import Union
from datetime import datetime


class ChatSessionsModel(BaseModel):
    
    id: str
    chat_id: str
    parent_id: Union[str, None]
    session_type: str
    started_at: Union[datetime, None]
    ended_at: Union[datetime, None]
    provider: str
    provider_uuid: Union[str, None]
    created_at: datetime
    updated_at: datetime




class ChatSessionsInitializer(BaseModel):
    
    id: Union[str, None] = None
    chat_id: str
    parent_id: str
    session_type: str
    started_at: datetime
    ended_at: datetime
    provider: str
    provider_uuid: Union[str, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None




class ChatSessionsUpdater(BaseModel):
    id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    parent_id: Union[str, None] = None 
    session_type: Union[str, None] = None 
    started_at: Union[datetime, None] = None 
    ended_at: Union[datetime, None] = None 
    provider: Union[str, None] = None 
    provider_uuid: Union[str, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    
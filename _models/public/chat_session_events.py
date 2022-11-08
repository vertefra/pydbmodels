from pydantic import BaseModel
from typing import Union, Any, Dict
from datetime import datetime


class ChatSessionEventsModel(BaseModel):
    
    id: str
    chat_id: str
    chat_session_id: str
    user_id: Union[str, None]
    event_type: str
    event_metadata: Union[Dict[str, Any],str, None]
    created_at: datetime




class ChatSessionEventsInitializer(BaseModel):
    
    id: Union[str, None] = None
    chat_id: str
    chat_session_id: str
    user_id: str
    event_type: str
    event_metadata: Union[Dict[str, Any], str]
    created_at: Union[datetime, None] = None




class ChatSessionEventsUpdater(BaseModel):
    id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    chat_session_id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    event_type: Union[str, None] = None 
    event_metadata: Union[Dict[str, Any], str, None] = None 
    created_at: Union[datetime, None] = None 
    
from pydantic import BaseModel
from datetime import datetime
from typing import Union, Any, Dict


class ChatSessionParticipantsModel(BaseModel):
    
    id: str
    chat_session_id: str
    chat_id: str
    user_id: str
    joined_at: datetime
    left_at: Union[datetime, None]
    stats: Union[Dict[str, Any],str, None]
    created_at: datetime
    updated_at: datetime




class ChatSessionParticipantsInitializer(BaseModel):
    
    id: Union[str, None] = None
    chat_session_id: str
    chat_id: str
    user_id: str
    joined_at: datetime
    left_at: datetime
    stats: Union[Dict[str, Any], str]
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None




class ChatSessionParticipantsUpdater(BaseModel):
    id: Union[str, None] = None 
    chat_session_id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    joined_at: Union[datetime, None] = None 
    left_at: Union[datetime, None] = None 
    stats: Union[Dict[str, Any], str, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    
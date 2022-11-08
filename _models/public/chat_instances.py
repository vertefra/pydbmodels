from pydantic import BaseModel
from datetime import datetime
from typing import Union


class ChatInstancesModel(BaseModel):
    
    id: str
    scheduled_start: datetime
    chat_id: str
    topic_id: str
    leader_user_id: str
    duration: int
    max_member_count: int
    breakout_duration: int
    prompt: Union[str, None]
    canceled_at: Union[datetime, None]
    created_at: datetime
    updated_at: datetime
    scheduled_end: Union[datetime, None]




class ChatInstancesInitializer(BaseModel):
    
    id: Union[str, None] = None
    scheduled_start: datetime
    chat_id: str
    topic_id: str
    leader_user_id: str
    duration: Union[int, None] = None
    max_member_count: int
    breakout_duration: Union[int, None] = None
    prompt: str
    canceled_at: datetime
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    scheduled_end: datetime




class ChatInstancesUpdater(BaseModel):
    id: Union[str, None] = None 
    scheduled_start: Union[datetime, None] = None 
    chat_id: Union[str, None] = None 
    topic_id: Union[str, None] = None 
    leader_user_id: Union[str, None] = None 
    duration: Union[int, None] = None 
    max_member_count: Union[int, None] = None 
    breakout_duration: Union[int, None] = None 
    prompt: Union[str, None] = None 
    canceled_at: Union[datetime, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    scheduled_end: Union[datetime, None] = None 
    
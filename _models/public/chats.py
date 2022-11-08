from pydantic import BaseModel
from datetime import datetime
from typing import Union, List, Any, Dict


class ChatsModel(BaseModel):
    
    id: str
    topic_id: str
    leader_user_id: str
    start_date: datetime
    end_date: Union[datetime, None]
    duration: int
    max_member_count: int
    breakout_duration: int
    images: Union[Dict[str, Any],str, None]
    tag_ids: Union[Union[List[Dict[str, Any]], List[str]], None]
    canceled_at: Union[datetime, None]
    created_at: datetime
    updated_at: datetime
    timezone: str
    recurring_time: str
    metadata: Union[Dict[str, Any],str, None]
    asset_id: Union[str, None]




class ChatsInitializer(BaseModel):
    
    id: Union[str, None] = None
    topic_id: str
    leader_user_id: str
    start_date: datetime
    end_date: datetime
    duration: int
    max_member_count: int
    breakout_duration: int
    images: Union[Dict[str, Any], str]
    tag_ids: Union[List[Dict[str, Any]], List[str]]
    canceled_at: datetime
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    timezone: Union[str, None] = None
    recurring_time: str
    metadata: Union[Dict[str, Any], str]
    asset_id: str




class ChatsUpdater(BaseModel):
    id: Union[str, None] = None 
    topic_id: Union[str, None] = None 
    leader_user_id: Union[str, None] = None 
    start_date: Union[datetime, None] = None 
    end_date: Union[datetime, None] = None 
    duration: Union[int, None] = None 
    max_member_count: Union[int, None] = None 
    breakout_duration: Union[int, None] = None 
    images: Union[Dict[str, Any], str, None] = None 
    tag_ids: Union[Union[List[Dict[str, Any]], List[str]], None] = None 
    canceled_at: Union[datetime, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    timezone: Union[str, None] = None 
    recurring_time: Union[str, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    asset_id: Union[str, None] = None 
    
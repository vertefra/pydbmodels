from pydantic import BaseModel
from typing import Union, List, Any, Dict
from datetime import datetime


class UserNodesModel(BaseModel):
    
    id: str
    user_id: str
    chat_ids: List[str]
    interest_ids: List[str]
    followed_ids: List[str]
    group_ids: List[str]
    close_preferences: Union[Dict[str, Any],str, None]
    location: Union[str, None]
    created_at: datetime
    updated_at: datetime




class UserNodesInitializer(BaseModel):
    
    id: Union[str, None] = None
    user_id: str
    chat_ids: Union[List[str], None] = None
    interest_ids: Union[List[str], None] = None
    followed_ids: Union[List[str], None] = None
    group_ids: Union[List[str], None] = None
    close_preferences: Union[Dict[str, Any], str]
    location: str
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None




class UserNodesUpdater(BaseModel):
    id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    chat_ids: Union[List[str], None] = None 
    interest_ids: Union[List[str], None] = None 
    followed_ids: Union[List[str], None] = None 
    group_ids: Union[List[str], None] = None 
    close_preferences: Union[Dict[str, Any], str, None] = None 
    location: Union[str, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    
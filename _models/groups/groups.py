from pydantic import BaseModel
from typing import Union, Any, Dict
from datetime import datetime


class GroupsModel(BaseModel):
    
    id: str
    topic_id: str
    group_type: str
    leader_user_id: str
    visibility: str
    deleted_at: Union[datetime, None]
    created_at: Union[datetime, None]
    metadata: Union[Dict[str, Any],str, None]




class GroupsInitializer(BaseModel):
    
    id: Union[str, None] = None
    topic_id: str
    group_type: Union[str, None] = None
    leader_user_id: str
    visibility: Union[str, None] = None
    deleted_at: datetime
    created_at: Union[datetime, None] = None
    metadata: Union[Dict[str, Any], str]




class GroupsUpdater(BaseModel):
    id: Union[str, None] = None 
    topic_id: Union[str, None] = None 
    group_type: Union[str, None] = None 
    leader_user_id: Union[str, None] = None 
    visibility: Union[str, None] = None 
    deleted_at: Union[datetime, None] = None 
    created_at: Union[datetime, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    
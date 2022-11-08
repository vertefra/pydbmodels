from pydantic import BaseModel
from typing import Union
from datetime import datetime


class GroupActivitiesModel(BaseModel):
    
    id: str
    group_id: str
    chat_id: Union[str, None]
    member_id: Union[str, None]
    activity: str
    timestamp: Union[datetime, None]




class GroupActivitiesInitializer(BaseModel):
    
    id: Union[str, None] = None
    group_id: str
    chat_id: str
    member_id: str
    activity: str
    timestamp: Union[datetime, None] = None




class GroupActivitiesUpdater(BaseModel):
    id: Union[str, None] = None 
    group_id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    member_id: Union[str, None] = None 
    activity: Union[str, None] = None 
    timestamp: Union[datetime, None] = None 
    
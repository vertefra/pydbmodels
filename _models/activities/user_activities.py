from pydantic import BaseModel
from typing import Union
from datetime import datetime


class UserActivitiesModel(BaseModel):
    
    id: str
    user_id: str
    activity: Union[str, None]
    group_id: Union[str, None]
    chat_id: Union[str, None]
    user_followed_id: Union[str, None]
    timestamp: Union[datetime, None]
    interest_id: Union[str, None]




class UserActivitiesInitializer(BaseModel):
    
    id: Union[str, None] = None
    user_id: str
    activity: str
    group_id: str
    chat_id: str
    user_followed_id: str
    timestamp: Union[datetime, None] = None
    interest_id: str




class UserActivitiesUpdater(BaseModel):
    id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    activity: Union[str, None] = None 
    group_id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    user_followed_id: Union[str, None] = None 
    timestamp: Union[datetime, None] = None 
    interest_id: Union[str, None] = None 
    
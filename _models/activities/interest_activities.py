from pydantic import BaseModel
from typing import Union
from datetime import datetime


class InterestActivitiesModel(BaseModel):
    
    id: str
    interest_id: str
    chat_id: Union[str, None]
    follower_id: Union[str, None]
    activity: str
    timestamp: Union[datetime, None]




class InterestActivitiesInitializer(BaseModel):
    
    id: Union[str, None] = None
    interest_id: str
    chat_id: str
    follower_id: str
    activity: str
    timestamp: Union[datetime, None] = None




class InterestActivitiesUpdater(BaseModel):
    id: Union[str, None] = None 
    interest_id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    follower_id: Union[str, None] = None 
    activity: Union[str, None] = None 
    timestamp: Union[datetime, None] = None 
    
from pydantic import BaseModel
from datetime import datetime
from typing import Union


class TopicsModel(BaseModel):
    
    id: str
    created_at: datetime
    updated_at: datetime
    name: str
    description: Union[str, None]
    short_description: Union[str, None]




class TopicsInitializer(BaseModel):
    
    id: Union[str, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    name: str
    description: str
    short_description: str




class TopicsUpdater(BaseModel):
    id: Union[str, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    name: Union[str, None] = None 
    description: Union[str, None] = None 
    short_description: Union[str, None] = None 
    
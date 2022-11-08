from pydantic import BaseModel
from typing import Union


class TopicsModel(BaseModel):
    
    id: str
    topic_uid: Union[str, None]
    name: Union[str, None]
    description: Union[str, None]




class TopicsInitializer(BaseModel):
    
    id: Union[str, None] = None
    topic_uid: str
    name: str
    description: str




class TopicsUpdater(BaseModel):
    id: Union[str, None] = None 
    topic_uid: Union[str, None] = None 
    name: Union[str, None] = None 
    description: Union[str, None] = None 
    
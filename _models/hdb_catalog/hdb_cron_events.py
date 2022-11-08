from pydantic import BaseModel
from datetime import datetime
from typing import Union


class HdbCronEventsModel(BaseModel):
    
    id: str
    trigger_name: str
    scheduled_time: datetime
    status: str
    tries: int
    created_at: Union[datetime, None]
    next_retry_at: Union[datetime, None]




class HdbCronEventsInitializer(BaseModel):
    
    id: Union[str, None] = None
    trigger_name: str
    scheduled_time: datetime
    status: Union[str, None] = None
    tries: Union[int, None] = None
    created_at: Union[datetime, None] = None
    next_retry_at: datetime




class HdbCronEventsUpdater(BaseModel):
    id: Union[str, None] = None 
    trigger_name: Union[str, None] = None 
    scheduled_time: Union[datetime, None] = None 
    status: Union[str, None] = None 
    tries: Union[int, None] = None 
    created_at: Union[datetime, None] = None 
    next_retry_at: Union[datetime, None] = None 
    
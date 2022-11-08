from pydantic import BaseModel
from typing import Union, Any, Dict
from datetime import datetime


class HdbScheduledEventInvocationLogsModel(BaseModel):
    
    id: str
    event_id: Union[str, None]
    status: Union[int, None]
    request: Union[Dict[str, Any],str, None]
    response: Union[Dict[str, Any],str, None]
    created_at: Union[datetime, None]




class HdbScheduledEventInvocationLogsInitializer(BaseModel):
    
    id: Union[str, None] = None
    event_id: str
    status: int
    request: Union[Dict[str, Any], str]
    response: Union[Dict[str, Any], str]
    created_at: Union[datetime, None] = None




class HdbScheduledEventInvocationLogsUpdater(BaseModel):
    id: Union[str, None] = None 
    event_id: Union[str, None] = None 
    status: Union[int, None] = None 
    request: Union[Dict[str, Any], str, None] = None 
    response: Union[Dict[str, Any], str, None] = None 
    created_at: Union[datetime, None] = None 
    
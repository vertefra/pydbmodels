from pydantic import BaseModel
from typing import Union, Any, Dict
from datetime import datetime


class HdbCronEventInvocationLogsModel(BaseModel):
    
    id: str
    event_id: Union[str, None]
    status: Union[int, None]
    request: Union[Dict[str, Any],str, None]
    response: Union[Dict[str, Any],str, None]
    created_at: Union[datetime, None]




class HdbCronEventInvocationLogsInitializer(BaseModel):
    
    id: Union[str, None] = None
    event_id: str
    status: int
    request: Union[Dict[str, Any], str]
    response: Union[Dict[str, Any], str]
    created_at: Union[datetime, None] = None




class HdbCronEventInvocationLogsUpdater(BaseModel):
    id: Union[str, None] = None 
    event_id: Union[str, None] = None 
    status: Union[int, None] = None 
    request: Union[Dict[str, Any], str, None] = None 
    response: Union[Dict[str, Any], str, None] = None 
    created_at: Union[datetime, None] = None 
    
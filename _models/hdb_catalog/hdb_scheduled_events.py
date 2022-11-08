from pydantic import BaseModel
from typing import Union, Any, Dict
from datetime import datetime


class HdbScheduledEventsModel(BaseModel):
    
    id: str
    webhook_conf: Dict[str, Any]
    scheduled_time: datetime
    retry_conf: Union[Dict[str, Any],str, None]
    payload: Union[Dict[str, Any],str, None]
    header_conf: Union[Dict[str, Any],str, None]
    status: str
    tries: int
    created_at: Union[datetime, None]
    next_retry_at: Union[datetime, None]
    comment: Union[str, None]




class HdbScheduledEventsInitializer(BaseModel):
    
    id: Union[str, None] = None
    webhook_conf: Union[Dict[str, Any], str]
    scheduled_time: datetime
    retry_conf: Union[Dict[str, Any], str]
    payload: Union[Dict[str, Any], str]
    header_conf: Union[Dict[str, Any], str]
    status: Union[str, None] = None
    tries: Union[int, None] = None
    created_at: Union[datetime, None] = None
    next_retry_at: datetime
    comment: str




class HdbScheduledEventsUpdater(BaseModel):
    id: Union[str, None] = None 
    webhook_conf: Union[Dict[str, Any], str, None] = None 
    scheduled_time: Union[datetime, None] = None 
    retry_conf: Union[Dict[str, Any], str, None] = None 
    payload: Union[Dict[str, Any], str, None] = None 
    header_conf: Union[Dict[str, Any], str, None] = None 
    status: Union[str, None] = None 
    tries: Union[int, None] = None 
    created_at: Union[datetime, None] = None 
    next_retry_at: Union[datetime, None] = None 
    comment: Union[str, None] = None 
    
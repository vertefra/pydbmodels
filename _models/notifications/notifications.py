from pydantic import BaseModel
from datetime import datetime
from typing import Union, Any, Dict


class NotificationsModel(BaseModel):
    
    id: str
    job_id: str
    chat_instance_id: str
    trigger_name: str
    trigger_at: datetime
    metadata: Union[Dict[str, Any],str, None]
    response: Union[str, None]
    triggered_at: Union[datetime, None]
    deleted_at: Union[datetime, None]




class NotificationsInitializer(BaseModel):
    
    id: Union[str, None] = None
    job_id: str
    chat_instance_id: str
    trigger_name: str
    trigger_at: datetime
    metadata: Union[Dict[str, Any], str]
    response: str
    triggered_at: datetime
    deleted_at: datetime




class NotificationsUpdater(BaseModel):
    id: Union[str, None] = None 
    job_id: Union[str, None] = None 
    chat_instance_id: Union[str, None] = None 
    trigger_name: Union[str, None] = None 
    trigger_at: Union[datetime, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    response: Union[str, None] = None 
    triggered_at: Union[datetime, None] = None 
    deleted_at: Union[datetime, None] = None 
    
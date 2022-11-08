from pydantic import BaseModel
from typing import Union, Any, Dict
from datetime import datetime


class HdbSchemaNotificationsModel(BaseModel):
    
    id: int
    notification: Dict[str, Any]
    resource_version: int
    instance_id: str
    updated_at: Union[datetime, None]




class HdbSchemaNotificationsInitializer(BaseModel):
    
    id: int
    notification: Union[Dict[str, Any], str]
    resource_version: Union[int, None] = None
    instance_id: str
    updated_at: Union[datetime, None] = None




class HdbSchemaNotificationsUpdater(BaseModel):
    id: Union[int, None] = None 
    notification: Union[Dict[str, Any], str, None] = None 
    resource_version: Union[int, None] = None 
    instance_id: Union[str, None] = None 
    updated_at: Union[datetime, None] = None 
    
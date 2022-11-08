from pydantic import BaseModel
from typing import Union, Any, Dict


class CustomerioTriggersModel(BaseModel):
    
    id: str
    trigger_name: str
    description: Union[str, None]
    trigger_id: Union[int, None]
    medium: Union[str, None]
    metadata: Union[Dict[str, Any],str, None]
    trigger_type: str




class CustomerioTriggersInitializer(BaseModel):
    
    id: Union[str, None] = None
    trigger_name: str
    description: str
    trigger_id: int
    medium: str
    metadata: Union[Dict[str, Any], str]
    trigger_type: str




class CustomerioTriggersUpdater(BaseModel):
    id: Union[str, None] = None 
    trigger_name: Union[str, None] = None 
    description: Union[str, None] = None 
    trigger_id: Union[int, None] = None 
    medium: Union[str, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    trigger_type: Union[str, None] = None 
    
from pydantic import BaseModel
from typing import Union, Any, Dict
from datetime import datetime


class HdbActionLogModel(BaseModel):
    
    id: str
    action_name: Union[str, None]
    input_payload: Dict[str, Any]
    request_headers: Dict[str, Any]
    session_variables: Dict[str, Any]
    response_payload: Union[Dict[str, Any],str, None]
    errors: Union[Dict[str, Any],str, None]
    created_at: datetime
    response_received_at: Union[datetime, None]
    status: str




class HdbActionLogInitializer(BaseModel):
    
    id: Union[str, None] = None
    action_name: str
    input_payload: Union[Dict[str, Any], str]
    request_headers: Union[Dict[str, Any], str]
    session_variables: Union[Dict[str, Any], str]
    response_payload: Union[Dict[str, Any], str]
    errors: Union[Dict[str, Any], str]
    created_at: Union[datetime, None] = None
    response_received_at: datetime
    status: str




class HdbActionLogUpdater(BaseModel):
    id: Union[str, None] = None 
    action_name: Union[str, None] = None 
    input_payload: Union[Dict[str, Any], str, None] = None 
    request_headers: Union[Dict[str, Any], str, None] = None 
    session_variables: Union[Dict[str, Any], str, None] = None 
    response_payload: Union[Dict[str, Any], str, None] = None 
    errors: Union[Dict[str, Any], str, None] = None 
    created_at: Union[datetime, None] = None 
    response_received_at: Union[datetime, None] = None 
    status: Union[str, None] = None 
    
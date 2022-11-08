from pydantic import BaseModel
from datetime import datetime
from typing import Union, Any, Dict


class HdbVersionModel(BaseModel):
    
    hasura_uuid: str
    version: str
    upgraded_on: datetime
    cli_state: Dict[str, Any]
    console_state: Dict[str, Any]




class HdbVersionInitializer(BaseModel):
    
    hasura_uuid: Union[str, None] = None
    version: str
    upgraded_on: datetime
    cli_state: Union[Dict[str, Any], str, None] = None
    console_state: Union[Dict[str, Any], str, None] = None




class HdbVersionUpdater(BaseModel):
    hasura_uuid: Union[str, None] = None 
    version: Union[str, None] = None 
    upgraded_on: Union[datetime, None] = None 
    cli_state: Union[Dict[str, Any], str, None] = None 
    console_state: Union[Dict[str, Any], str, None] = None 
    
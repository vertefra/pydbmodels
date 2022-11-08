from pydantic import BaseModel
from typing import Union, Any, Dict


class RolesModel(BaseModel):
    
    id: str
    role_name: str
    metadata: Union[Dict[str, Any],str, None]




class RolesInitializer(BaseModel):
    
    id: Union[str, None] = None
    role_name: str
    metadata: Union[Dict[str, Any], str]




class RolesUpdater(BaseModel):
    id: Union[str, None] = None 
    role_name: Union[str, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    
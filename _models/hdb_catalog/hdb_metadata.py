from pydantic import BaseModel
from typing import Union, Any, Dict


class HdbMetadataModel(BaseModel):
    
    id: int
    metadata: Dict[str, Any]
    resource_version: int




class HdbMetadataInitializer(BaseModel):
    
    id: int
    metadata: Union[Dict[str, Any], str]
    resource_version: Union[int, None] = None




class HdbMetadataUpdater(BaseModel):
    id: Union[int, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    resource_version: Union[int, None] = None 
    
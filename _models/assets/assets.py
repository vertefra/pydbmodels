from pydantic import BaseModel
from typing import Union, Any, Dict


class AssetsModel(BaseModel):
    
    id: str
    asset_name: str
    metadata: Dict[str, Any]




class AssetsInitializer(BaseModel):
    
    id: Union[str, None] = None
    asset_name: str
    metadata: Union[Dict[str, Any], str]




class AssetsUpdater(BaseModel):
    id: Union[str, None] = None 
    asset_name: Union[str, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    
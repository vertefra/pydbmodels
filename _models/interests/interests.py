from pydantic import BaseModel
from typing import Union, Any, Dict


class InterestsModel(BaseModel):
    
    id: str
    interest_name: str
    metadata: Union[Dict[str, Any],str, None]
    description: Union[str, None]




class InterestsInitializer(BaseModel):
    
    id: Union[str, None] = None
    interest_name: str
    metadata: Union[Dict[str, Any], str]
    description: str




class InterestsUpdater(BaseModel):
    id: Union[str, None] = None 
    interest_name: Union[str, None] = None 
    metadata: Union[Dict[str, Any], str, None] = None 
    description: Union[str, None] = None 
    
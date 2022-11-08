from pydantic import BaseModel
from typing import Union


class InterestAssetsModel(BaseModel):
    
    id: str
    asset_id: Union[str, None]
    interest_id: Union[str, None]




class InterestAssetsInitializer(BaseModel):
    
    id: Union[str, None] = None
    asset_id: str
    interest_id: str




class InterestAssetsUpdater(BaseModel):
    id: Union[str, None] = None 
    asset_id: Union[str, None] = None 
    interest_id: Union[str, None] = None 
    
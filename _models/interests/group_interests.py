from pydantic import BaseModel


class GroupInterestsModel(BaseModel):
    
    id: str
    group_id: str
    interest_id: str




class GroupInterestsInitializer(BaseModel):
    
    id: Union[str, None] = None
    group_id: str
    interest_id: str




class GroupInterestsUpdater(BaseModel):
    id: Union[str, None] = None 
    group_id: Union[str, None] = None 
    interest_id: Union[str, None] = None 
    
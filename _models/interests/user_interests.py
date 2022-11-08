from pydantic import BaseModel


class UserInterestsModel(BaseModel):
    
    id: str
    user_id: str
    interest_id: str




class UserInterestsInitializer(BaseModel):
    
    id: Union[str, None] = None
    user_id: str
    interest_id: str




class UserInterestsUpdater(BaseModel):
    id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    interest_id: Union[str, None] = None 
    
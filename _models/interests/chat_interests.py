from pydantic import BaseModel


class ChatInterestsModel(BaseModel):
    
    id: str
    chat_id: str
    interest_id: str




class ChatInterestsInitializer(BaseModel):
    
    id: Union[str, None] = None
    chat_id: str
    interest_id: str




class ChatInterestsUpdater(BaseModel):
    id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    interest_id: Union[str, None] = None 
    
from pydantic import BaseModel


class ChatUserRolesModel(BaseModel):
    
    id: str
    chat_id: str
    user_id: str
    role_id: str




class ChatUserRolesInitializer(BaseModel):
    
    id: Union[str, None] = None
    chat_id: str
    user_id: str
    role_id: str




class ChatUserRolesUpdater(BaseModel):
    id: Union[str, None] = None 
    chat_id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    role_id: Union[str, None] = None 
    
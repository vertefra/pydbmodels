from pydantic import BaseModel
from datetime import datetime


class AdminUsersModel(BaseModel):
    
    id: str
    name: str
    email: str
    password: str
    super_user: bool
    created_at: datetime
    updated_at: datetime




class AdminUsersInitializer(BaseModel):
    
    id: Union[str, None] = None
    name: str
    email: str
    password: str
    super_user: Union[bool, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None




class AdminUsersUpdater(BaseModel):
    id: Union[str, None] = None 
    name: Union[str, None] = None 
    email: Union[str, None] = None 
    password: Union[str, None] = None 
    super_user: Union[bool, None] = None 
    created_at: Union[datetime, None] = None 
    updated_at: Union[datetime, None] = None 
    
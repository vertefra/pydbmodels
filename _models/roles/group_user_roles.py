from pydantic import BaseModel


class GroupUserRolesModel(BaseModel):
    
    id: str
    group_id: str
    user_id: str
    role_id: str




class GroupUserRolesInitializer(BaseModel):
    
    id: Union[str, None] = None
    group_id: str
    user_id: str
    role_id: str




class GroupUserRolesUpdater(BaseModel):
    id: Union[str, None] = None 
    group_id: Union[str, None] = None 
    user_id: Union[str, None] = None 
    role_id: Union[str, None] = None 
    
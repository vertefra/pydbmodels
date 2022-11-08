from pydantic import BaseModel


class SchemaMigrationsModel(BaseModel):
    
    version: str




class SchemaMigrationsInitializer(BaseModel):
    
    version: str




class SchemaMigrationsUpdater(BaseModel):
    version: Union[str, None] = None 
    
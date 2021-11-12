from pydantic import BaseModel
from typing   import Optional, List

class Role(BaseModel):
    
    id         : Optional[str] = None
    name       : str

    class Config():
        orm_mode = True

class User(BaseModel):

    id         : Optional[str] = None
    username   : str
    picture    : str
    stars      : int
    type       : str
    cellphone  : str
    password   : str

    class Config():
        orm_mode = True

class Team(BaseModel):

    id         : Optional[str] = None        
    name       : str
    color      : str
    picture    : str

    class Config():
        orm_mode = True


class TeamPlayer(BaseModel):

    id         : Optional[str] = None         
    id_team    : int
    id_user    : int
    date       : str
    team       : List[Team]
    player     : List[User]

    class Config():
        orm_mode = True


class Match(BaseModel):

    id                     : Optional[str] = None                   
    id_team_one            : int
    id_team_two            : int
    match_status_team_one  : str
    match_status_team_two  : str
    match_date             : str

    class Config():
        orm_mode = True

    
class Statistic(BaseModel):
    
    id         : Optional[str] = None           
    id_user    : int       
    date       : str   
    status     : str    

    class Config():
        orm_mode = True        

class RoleUser(BaseModel):
    
    id         : Optional[str] = None        
    id_role    : int
    id_user    : int
    role       : List[Role]       
    user       : List[Role]   

    class Config():
        orm_mode = True     





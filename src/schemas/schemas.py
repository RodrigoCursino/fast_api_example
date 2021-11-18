from pydantic import BaseModel
from typing   import Optional, List
from sqlalchemy.sql import roles

from sqlalchemy.sql.functions import user

# -------- USER -------- #
class Role(BaseModel):
    
    id         : Optional[int] = None
    name       : str

    class Config():
        orm_mode = True

class RoleByUser(BaseModel):
    
    id         : Optional[int] = None        
    role       : Role 

class User(BaseModel):

    id         : Optional[int] = None
    username   : str
    picture    : str
    stars      : int
    cellphone  : str
    password   : str
    roles      : List[RoleByUser] = []

    class Config():
        orm_mode = True

class UserLogin(BaseModel):
    
    cellphone  : str
    password   : str
 
class RoleUser(BaseModel):
    
    id         : Optional[int] = None        
    id_role    : int
    id_user    : int
    role       : List[Role]       
    user       : List[User]   

    class Config():
        orm_mode = True   
# -------- USER -------- #  

# -------- Match -------- #
class Team(BaseModel):

    id         : Optional[int] = None        
    name       : str
    color      : str
    picture    : str
    #players    : List[User] = []

    class Config():
        orm_mode = True


class TeamPlayer(BaseModel):

    id         : Optional[int] = None         
    id_team    : int
    id_user    : int
    date       : str
    team       : List[Team]
    player     : List[User]

    class Config():
        orm_mode = True


class Match(BaseModel):

    id                     : Optional[int] = None                   
    id_team_one            : int
    id_team_two            : int
    match_status_team_one  : str
    match_status_team_two  : str
    match_date             : str

    class Config():
        orm_mode = True

    
class Statistic(BaseModel):
    
    id         : Optional[int] = None           
    id_user    : int       
    date       : str   
    status     : str 
    match      : List[Match]   
    user       : List[Match]

    class Config():
        orm_mode = True  

# -------- Match -------- #      







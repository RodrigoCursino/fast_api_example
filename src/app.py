from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from src.infra.sqlalchemy.repositories.team import TeamRepository
from src.infra.sqlalchemy.config.database   import get_db
from src.schemas.schemas import Team

api = FastAPI()

@api.post('/teams')
def store(team: Team, db: Session = Depends(get_db)):
    return TeamRepository(db).store(team)

@api.get('/teams')
def list_all(db: Session = Depends(get_db)):
    return TeamRepository(db).list()

@api.get('/team-by-id')
def list_all(id:int, db: Session = Depends(get_db)):
    return TeamRepository(db).get(id)
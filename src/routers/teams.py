from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from src.infra.sqlalchemy.repositories.team import TeamRepository
from src.infra.sqlalchemy.config.database   import get_db
from src.schemas.schemas import Team

router = APIRouter(
    prefix="/teams",
    tags=["teams"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post('', status_code=status.HTTP_201_CREATED, response_model=Team)
def store(team: Team, db: Session = Depends(get_db)):
    return TeamRepository(db).store(team)

@router.get('')
def list_all(db: Session = Depends(get_db)):
    return TeamRepository(db).list()

@router.get('/get', response_model=Team)
def list_all(id:int, db: Session = Depends(get_db)):
    return TeamRepository(db).get(id)
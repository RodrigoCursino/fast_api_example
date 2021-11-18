from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session

from src.infra.sqlalchemy.repositories.user import UserRepository
from src.infra.sqlalchemy.config.database   import get_db
from src.schemas                            import schemas

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post('/login', status_code=status.HTTP_200_OK)
def signin(model: schemas.UserLogin, db: Session = Depends(get_db)):
    return UserRepository(db).login(model)



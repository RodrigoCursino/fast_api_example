from src.schemas                        import schemas
from src.infra.sqlalchemy.models        import models
from sqlalchemy.orm                     import Session

class TeamRepository():
    
    def __init__(self, db: Session):
        self.db = db

    def list(self):
        return self.db.query(models.Team).all()

    def get(self,id):
        return self.db.query(models.Team).filter(models.Team.id == id).first()

    def store(self, team: schemas.Team):
        
        db_team = models.Team(
            name=team.name,
            color=team.color, 
            picture=team.picture
        )

        self.db.add(db_team)
        self.db.commit()
        self.db.refresh(db_team)

        return db_team

    def update(self):
        pass
    
    def delete(self):
        pass


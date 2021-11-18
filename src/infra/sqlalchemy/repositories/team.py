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

    def store(self, model: schemas.Team):
        
        db_model = models.Team(
            name=model.name,
            color=model.color, 
            picture=model.picture
        )

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return db_model

    def update(self):
        pass
    
    def delete(self):
        pass


from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models


def create_establishment(db: Session, establishment: schemas.EstablishmentCreate):
    db_establishment = models.Establishment(**establishment.dict())
    db.add(db_establishment)
    db.commit()
    db.refresh(db_establishment)
    return db_establishment


def get_establishments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Establishment).offset(skip).limit(limit).all()


def get_establishment(db: Session, establishment_id: int):
    return db.query(models.Establishment).filter(models.Establishment.id == establishment_id).first()


def delete_establishment(db: Session, establishment_id: int):
    establishment = db.query(models.Establishment).filter(models.Establishment.id == establishment_id).first()
    if establishment:
        db.delete(establishment)
        db.commit()
        return True
    return False

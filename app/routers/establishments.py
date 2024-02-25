from app.schemas import schemas
from app.crud import establishments

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.db import database

router = APIRouter(prefix="/establishments", tags=["establishments"])


@router.post("/", response_model=schemas.Establishment)
def create_establishment(establishment: schemas.EstablishmentCreate, db: Session = Depends(database.get_db)):
    return establishments.create_establishment(db=db, establishment=establishment)


@router.get("/", response_model=List[schemas.Establishment])
def get_establishments(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return establishments.get_establishments(db=db, skip=skip, limit=limit)


@router.get("/{establishment_id}", response_model=schemas.Establishment)
def get_establishment(establishment_id: int, db: Session = Depends(database.get_db)):
    db_establishment = establishments.get_establishment(db=db, establishment_id=establishment_id)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Establishment not found")
    return db_establishment


@router.delete("/{establishment_id}", response_model=schemas.Message)
def delete_establishment(establishment_id: int, db: Session = Depends(database.get_db)):
    db_establishment = establishments.get_establishment(db=db, establishment_id=establishment_id)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Establishment not found")
    establishments.delete_establishment(db=db, establishment_id=establishment_id)
    return {"message": "Establishment deleted successfully"}

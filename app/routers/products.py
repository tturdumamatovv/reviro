from app.schemas import schemas
from app.crud import products


from fastapi import Depends, HTTPException, APIRouter
from typing import List
from sqlalchemy.orm import Session

from app.db import database


router = APIRouter(prefix="/products", tags=["products"])


@router.post("", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return products.create_product(db=db, product=product)


@router.get("", response_model=List[schemas.Product])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return products.get_products(db=db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(database.get_db)):
    product = products.get_product(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{product_id}", response_model=schemas.Message)
def delete_product(product_id: int, db: Session = Depends(database.get_db)):
    result = products.delete_product(db=db, product_id=product_id)
    if result.get("message") == "Product not found":
        raise HTTPException(status_code=404, detail="Product not found")
    return result

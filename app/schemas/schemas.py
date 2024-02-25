from pydantic import BaseModel
from typing import List


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity_in_stock: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class EstablishmentBase(BaseModel):
    name: str
    description: str
    locations: str
    opening_hours: str


class EstablishmentCreate(EstablishmentBase):
    pass


class Establishment(EstablishmentBase):
    id: int

    class Config:
        orm_mode = True


class Message(BaseModel):
    message: str
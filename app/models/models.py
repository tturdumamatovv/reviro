from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class Establishment(Base):
    __tablename__ = 'establishments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    locations = Column(String)
    opening_hours = Column(String)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity_in_stock = Column(Integer, default=0)

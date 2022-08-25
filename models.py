from database import Base
from sqlalchemy import Column, Integer, Float


class Customer(Base):
    __tablename__ = "advertising"

    CustomerID = Column(Integer, primary_key=True)
    TV = Column(Float)
    Radio = Column(Float)
    Newspaper = Column(Float)
    Sales = Column(Float)
from pydantic import BaseModel
from typing import Optional


class Customer(BaseModel):
    TV: float
    Radio: float
    Newspaper: float
    Sales: float


class Advertising(BaseModel):
    TV: float
    Radio: float
    Newspaper: float



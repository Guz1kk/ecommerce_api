from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class OrderBase(BaseModel):
    order_date: Optional[datetime] = None
    total_amount: float

class OrderCreate(OrderBase):
    customer_id: int

class Order(OrderBase):
    id: int
    customer_id: int

    class Config:
        from_attributes = True

class CustomerBase(BaseModel):
    name: str
    surname: str
    email: EmailStr

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    orders: List[Order] = []

    class Config:
        from_attributes = True

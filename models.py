from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    orders = relationship('Order', back_populates='customer')


class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Numeric(10, 2), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    
    customer = relationship('Customer', back_populates='orders')
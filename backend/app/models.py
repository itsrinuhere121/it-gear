from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from database import Base
from sqlalchemy.orm import relationship

class Equipment(Base):
    __tablename__ = "Equipment"
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    category = Column(String(20))
    status = Column(String(30), default="available")  # Default value for status
    checkouts = relationship("Checkout", back_populates="equipment")  # Define the relationship
class Employee(Base):
    __tablename__ = "Employees"
    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    department = Column(String(30))
    checkouts = relationship("Checkout", back_populates="employee")
    
class Checkout(Base):
    __tablename__ = "Checkouts"
    checkout_id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("Equipment.item_id", ondelete='CASCADE'))
    emp_id = Column(Integer, ForeignKey("Employees.emp_id"))
    checkout_date = Column(Date)
    due_date = Column(Date)
    return_date = Column(Date, nullable=True)
    is_reservation = Column(Boolean, default=False)
    equipment = relationship("Equipment", back_populates="checkouts")
    employee = relationship("Employee", back_populates="checkouts")
    
    __table_args__ = {'mysql_engine': 'InnoDB'}
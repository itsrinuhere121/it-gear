from pydantic import BaseModel
from datetime import date
from typing import Optional

# Equipment Schemas
class EquipmentBase(BaseModel):
    item_id: int
    name: str
    category: str
    status: str
    class Config:
        from_attributes = True  # Use this for Pydantic v2 to work with SQLAlchemy models
class EquipmentUpdate(BaseModel):
    name: str
    category: str
    status: str
class EquipmentCreate(BaseModel):
    name: str
    category: str
    status: str = "available"

class Equipment(BaseModel):
    item_id: int
    status: str
    
    class Config:
        from_attributes = True  # Changed from orm_mode

# Employee Schemas
class EmployeeBase(BaseModel):
    emp_id: int
    name: str
    department: str
    class Config:
        from_attributes = True  # Use this for Pydantic v2 to work with SQLAlchemy models
class EmployeeResponse(EmployeeBase):  # Renamed from Employee
    emp_id: int

    class Config:
        from_attributes = True
class EmployeeCreate(EmployeeBase):
    name: str
    department: str

class Employee(EmployeeBase):
    emp_id: int
    
    class Config:
        from_attributes = True
class EmployeeResponse(EmployeeBase):
    pass
# Checkout Schemas
class CheckoutBase(BaseModel):
    item_id: int
    emp_id: int
    checkout_date: date
    due_date: date
    is_reservation: bool = False
    class Config:
        from_attributes = True  # Use this for Pydantic v2 to work with SQLAlchemy models
class CheckoutCreate(CheckoutBase):
    pass

class Checkout(CheckoutBase):
    checkout_id: int
    return_date: Optional[date] = None
    equipment: Optional[Equipment] = None
    employee: Optional[Employee] = None
    
    class Config:
        from_attributes = True
class CheckoutResponse(CheckoutBase):
    checkout_id: int
    item_id: int
    emp_id: int
    checkout_date: date
    due_date: date
    return_date: Optional[date] = None
    is_reservation: bool
    class Config:
        from_attributes = True  # Use this for Pydantic v2 to work with SQLAlchemy models
class UsageReport(BaseModel):
    period: str
    items: list[dict]  # List of dictionaries with item_id, name, and total_checkouts

    class Config:
        from_attributes = True  # Use this for Pydantic v2 to work with SQLAlchemy models



class EmployeeCreate(BaseModel):
    name: str
    department: str
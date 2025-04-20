from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Equipment, Checkout
from schemas import *
def checkout_equipment(db: Session, checkout: CheckoutCreate):
    # Check if equipment is available
    equipment = db.query(Equipment).filter(Equipment.item_id == checkout.item_id).first()
    if equipment.status != "available":
        raise HTTPException(status_code=400, detail="Equipment already checked out")
    
    # Create checkout record
    db_checkout = Checkout(**checkout.dict())
    db.add(db_checkout)
    
    # Update equipment status
    equipment.status = "checked out"
    db.commit()
    db.refresh(db_checkout)
    return db_checkout

from sqlalchemy.orm import Session
from datetime import date
from models import Equipment, Employee, Checkout

# Equipment operations
def get_equipment(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Equipment).offset(skip).limit(limit).all()
# Equipment CRUD
def create_equipment(db: Session, equipment: EquipmentCreate):
    db_equipment = Equipment(
        name=equipment.name,
        category=equipment.category
    )
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment
def get_available_equipment(db: Session):
    return db.query(Equipment).filter(Equipment.status == 'available').all()

# Employee operations
def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()

# Checkout operations
def create_checkout(db: Session, checkout: CheckoutCreate):
    equipment = db.query(Equipment).filter(Equipment.item_id == checkout.item_id).first()
    
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    if equipment.status != 'available':
        raise HTTPException(status_code=400, detail="Equipment already checked out")
    if checkout.checkout_date > checkout.due_date:
        raise HTTPException(status_code=400, detail="Due date must be after checkout date")
    
    db_checkout = Checkout(**checkout.dict())
    db.add(db_checkout)
    equipment.status = 'checked out'
    db.commit()
    db.refresh(db_checkout)
    return db_checkout

def return_equipment(db: Session, checkout_id: int):
    checkout = db.query(Checkout).filter(Checkout.checkout_id == checkout_id).first()
    if not checkout:
        raise HTTPException(status_code=404, detail="Checkout not found")
    
    equipment = db.query(Equipment).filter(Equipment.item_id == checkout.item_id).first()
    checkout.return_date = date.today()
    equipment.status = 'available'
    db.commit()
    return checkout

# Report operations
def get_overdue_checkouts(db: Session):
    today = date.today()
    return db.query(Checkout).filter(
        Checkout.return_date == None,
        Checkout.due_date < today
    ).all()

def get_usage_report(db: Session):
    # return db.query(Checkout).all()
    return [
        {"item_id": 1, "name": "Laptop1", "total_checkouts": 5},
        {"item_id": 2, "name": "Projector1", "total_checkouts": 3}
    ]
def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()

def update_employee(db: Session, emp_id: int, employee: EmployeeCreate):
    db_employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee
def delete_equipment(db: Session, item_id: int):
    db_equipment = db.query(Equipment).filter(Equipment.item_id == item_id).first()
    if not db_equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    db.delete(db_equipment)
    db.commit()
def update_equipment(db: Session, item_id: int, equipment: EquipmentUpdate):
    db_equipment = db.query(Equipment).filter(Equipment.item_id == item_id).first()
    if not db_equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    for key, value in equipment.dict().items():
        setattr(db_equipment, key, value)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment
def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
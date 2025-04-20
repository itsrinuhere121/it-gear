from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Checkout
from schemas import *
from schemas import *
from crud import *
app = FastAPI()  # Create the FastAPI app instance
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 # EQUIPMENT        
@app.get("/equipment/", response_model=list[EquipmentBase])
def read_equipment(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_equipment(db, skip=skip, limit=limit)

@app.post("/equipment/", response_model=EquipmentBase)
def create_new_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    return create_equipment(db=db, equipment=equipment)

@app.put("/equipment/{item_id}", response_model=EquipmentBase)
def update_existing_equipment(item_id: int, equipment: EquipmentUpdate, db: Session = Depends(get_db)):
    return update_equipment(db=db, item_id=item_id, equipment=equipment)

@app.delete("/equipment/{item_id}")
def delete_existing_equipment(item_id: int, db: Session = Depends(get_db)):
    delete_equipment(db=db, item_id=item_id)
    return {"message": "Equipment deleted successfully"}

@app.get("/equipment/available", response_model=list[EquipmentBase])
def read_available_equipment(db: Session = Depends(get_db)):
    return get_available_equipment(db)

# EMPLOYEE
@app.post("/employees/", response_model=EmployeeBase)
def create_new_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db=db, employee=employee)
@app.put("/employees/{emp_id}", response_model=EmployeeBase)
def update_existing_employee(emp_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    return update_employee(db=db, emp_id=emp_id, employee=employee)
@app.delete("/employees/{emp_id}")
def delete_existing_employee(emp_id: int, db: Session = Depends(get_db)):
    delete_employee(db=db, emp_id=emp_id)
    return {"message": "Employee deleted successfully"}
@app.get("/employees/", response_model=list[EmployeeResponse])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_employees(db, skip=skip, limit=limit)

@app.post("/checkouts/", response_model=CheckoutResponse)
def create_new_checkout(checkout: CheckoutCreate, db: Session = Depends(get_db)):
    return create_checkout(db=db, checkout=checkout)

@app.put("/checkouts/{checkout_id}/return", response_model=CheckoutResponse)
def return_checkout(checkout_id: int, db: Session = Depends(get_db)):
    return return_equipment(db=db, checkout_id=checkout_id)

@app.get("/reports/overdue", response_model=list[CheckoutResponse])
def get_overdue_report(db: Session = Depends(get_db)):
    return get_overdue_checkouts(db=db)
@app.get("/reports/usage", response_model=UsageReport)
def get_usage_statistics(db: Session = Depends(get_db)):
    return {"period": "monthly", "items": get_usage_report(db=db)}

app.include_router(router)  
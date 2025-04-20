Here are the cURL commands for testing all API endpoints based on your implementation:

### 1. Get All Equipment
```bash
curl -X 'GET' \
  'http://localhost:8000/equipment/' \
  -H 'accept: application/json'
```

### 2. Get Available Equipment
```bash
curl -X 'GET' \
  'http://localhost:8000/equipment/available' \
  -H 'accept: application/json'
```

### 3. Get All Employees
```bash
curl -X 'GET' \
  'http://localhost:8000/employees/' \
  -H 'accept: application/json'
```

### 4. Create Checkout (POST)
```bash
curl -X 'POST' \
  'http://localhost:8000/checkouts/' \
  -H 'Content-Type: application/json' \
  -d '{
    "item_id": 1,
    "emp_id": 1,
    "checkout_date": "2024-04-10",
    "due_date": "2024-04-17",
    "is_reservation": false
  }'
```

### 5. Return Equipment (PUT)
```bash
curl -X 'PUT' \
  'http://localhost:8000/checkouts/1/return' \
  -H 'accept: application/json'
```

### 6. Get Overdue Report
```bash
curl -X 'GET' \
  'http://localhost:8000/reports/overdue' \
  -H 'accept: application/json'
```

### 7. Get Usage Statistics
```bash
curl -X 'GET' \
  'http://localhost:8000/reports/usage' \
  -H 'accept: application/json'
```

---

### Complete Workflow Test
1. **Add Test Data First** (via DB client):
```sql
-- Equipment
INSERT INTO equipment (name, category) VALUES
('MacBook Pro', 'Laptop'),
('Epson Projector', 'Projector');

-- Employees
INSERT INTO employees (name, department) VALUES
('John Doe', 'IT'),
('Jane Smith', 'Marketing');
```

2. **Test Sequence**:
```bash
# 1. Check available equipment
curl -X GET http://localhost:8000/equipment/available

# 2. Create a checkout
curl -X POST http://localhost:8000/checkouts/ -H "Content-Type: application/json" -d '
{
    "item_id": 1,
    "emp_id": 1,
    "checkout_date": "2024-04-10",
    "due_date": "2024-04-12"
}'

# 3. Verify equipment status changed
curl -X GET http://localhost:8000/equipment/

# 4. Return equipment (replace {checkout_id} with actual ID)
curl -X PUT http://localhost:8000/checkouts/1/return

# 5. Check overdue report (should be empty after return)
curl -X GET http://localhost:8000/reports/overdue

# 6. Get usage statistics
curl -X GET http://localhost:8000/reports/usage
```

**Note**: Replace dates with current dates for meaningful overdue testing. For testing overdue items, create a checkout with a past due date:
```json
{
    "item_id": 2,
    "emp_id": 2,
    "checkout_date": "2024-04-01",
    "due_date": "2024-04-05"
}
```
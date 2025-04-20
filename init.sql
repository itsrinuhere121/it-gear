-- Create Database
CREATE DATABASE IF NOT EXISTS GearTrack;
USE GearTrack;

-- Equipment Table
CREATE TABLE Equipment (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(30) NOT NULL,
    status VARCHAR(30) DEFAULT 'available' CHECK (status IN ('available', 'checked out'))
);

-- Employees Table
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    department VARCHAR(30) NOT NULL
);

-- Checkouts Table
CREATE TABLE Checkouts (
    checkout_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    emp_id INT,
    checkout_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE DEFAULT NULL,
    is_reservation BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (item_id) REFERENCES Equipment(item_id),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id),
    CHECK (checkout_date <= due_date)
);

-- Trigger for Checkout
DELIMITER $$
CREATE TRIGGER after_checkout_insert
AFTER INSERT ON Checkouts
FOR EACH ROW
BEGIN
    UPDATE Equipment SET status = 'checked out' WHERE item_id = NEW.item_id;
END$$
DELIMITER ;

-- Trigger for Return
DELIMITER $$
CREATE TRIGGER after_return_update
AFTER UPDATE ON Checkouts
FOR EACH ROW
BEGIN
    IF NEW.return_date IS NOT NULL THEN
        UPDATE Equipment SET status = 'available' WHERE item_id = NEW.item_id;
    END IF;
END$$
DELIMITER ;

-- Ensure auto-increment is enabled
ALTER TABLE employees MODIFY emp_id INT AUTO_INCREMENT;
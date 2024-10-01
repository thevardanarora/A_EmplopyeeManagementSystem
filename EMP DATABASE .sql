CREATE DATABASE EmployeeDB;

USE EmployeeDB;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    position VARCHAR(50),
    salary DECIMAL(10, 2)
);
select * from employees;

import mysql.connector

# Connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # your MySQL username
        password="password",  # your MySQL password
        database="EmployeeDB"
    )

# Add a new employee to the database
def add_employee(first_name, last_name, age, position, salary):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO employees (first_name, last_name, age, position, salary) VALUES (%s, %s, %s, %s, %s)"
    values = (first_name, last_name, age, position, salary)
    cursor.execute(sql, values)
    db.commit()
    print(f"Employee {first_name} {last_name} added successfully!")
    cursor.close()
    db.close()

# View all employees in the database
def view_employees():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)
    cursor.close()
    db.close()

# Update employee information
def update_employee(emp_id, first_name=None, last_name=None, age=None, position=None, salary=None):
    db = connect_to_db()
    cursor = db.cursor()
    
    sql = "UPDATE employees SET "
    updates = []
    if first_name:
        updates.append(f"first_name = '{first_name}'")
    if last_name:
        updates.append(f"last_name = '{last_name}'")
    if age:
        updates.append(f"age = {age}")
    if position:
        updates.append(f"position = '{position}'")
    if salary:
        updates.append(f"salary = {salary}")
    
    sql += ", ".join(updates) + f" WHERE emp_id = {emp_id}"
    cursor.execute(sql)
    db.commit()
    print(f"Employee {emp_id} updated successfully!")
    cursor.close()
    db.close()

# Delete an employee from the database
def delete_employee(emp_id):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
    db.commit()
    print(f"Employee {emp_id} deleted successfully!")
    cursor.close()
    db.close()

# Main menu function
def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            position = input("Position: ")
            salary = float(input("Salary: "))
            add_employee(first_name, last_name, age, position, salary)
        
        elif choice == '2':
            view_employees()
        
        elif choice == '3':
            emp_id = int(input("Enter Employee ID to update: "))
            print("Leave the field blank if you don't want to change it.")
            first_name = input("New First Name: ") or None
            last_name = input("New Last Name: ") or None
            age = input("New Age: ")
            age = int(age) if age else None
            position = input("New Position: ") or None
            salary = input("New Salary: ")
            salary = float(salary) if salary else None
            update_employee(emp_id, first_name, last_name, age, position, salary)
        
        elif choice == '4':
            emp_id = int(input("Enter Employee ID to delete: "))
            delete_employee(emp_id)
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the system
menu()

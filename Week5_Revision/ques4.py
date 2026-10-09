employees = {
    "E101": {"name": "Ram", "department": "IT", "salary": 30000},
    "E102": {"name": "Sita", "department": "HR", "salary": 35000},
    "E103": {"name": "Hari", "department": "Sales", "salary": 25000},
    "E104": {"name": "Gita", "department": "Finance", "salary": 40000},
    "E105": {"name": "Shyam", "department": "IT", "salary": 45000}
}

# Find an employee
def find_employee(employee_id):
    if employee_id not in employees:
        raise KeyError("Employee ID does not exist.")
    return employees[employee_id]

# Calculate yearly salary
def yearly_salary(monthly_salary):
    return monthly_salary * 12

# Increase employee salary
def increase_salary(employee, percentage):
    if percentage < 0:
        raise ValueError("Percentage cannot be negative.")

    old_salary = employee["salary"]
    increase = old_salary * percentage / 100
    new_salary = old_salary + increase

    employee["salary"] = new_salary
    return old_salary, new_salary

# Ask the user for employee ID
employee_id = input("Enter employee ID: ").strip().upper()

try:
    employee = find_employee(employee_id)

    print("\nEmployee Name:", employee["name"])
    print("Department:", employee["department"])

    # Ask for salary increase percentage
    percentage = float(input("Enter salary increase percentage: "))

    old_salary, new_salary = increase_salary(employee, percentage)

    print("\n----- SALARY DETAILS -----")
    print("Old Monthly Salary: Rs.", old_salary)
    print("Salary Increase:", percentage, "%")
    print("New Monthly Salary: Rs.", round(new_salary, 2))
    print("Yearly Salary: Rs.", round(yearly_salary(new_salary), 2))

except KeyError as error:
    print("Error:", error)

except ValueError as error:
    print("Invalid percentage:", error)

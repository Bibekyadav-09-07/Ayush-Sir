employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}
del employee["age"]
del employee["city"]
print("Dictionary:", employee)
employee.pop("email", None)
print("After trying to remove email:", employee)
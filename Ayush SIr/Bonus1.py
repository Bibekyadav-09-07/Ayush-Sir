students = ["Ram", "Sita", "Hari", "Gita"]

marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92
}

# Display all students and marks
for student in students:
    print(student, "-", marks[student])

# Display students who scored 80 or above
print("\nStudents who scored 80 or above:")

for student in students:

    if marks[student] >= 80:
        print(student, "-", marks[student])
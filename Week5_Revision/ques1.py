students = [
    {"name": "Ram", "Math": 80, "English": 75, "Science": 85},
    {"name": "Sita", "Math": 90, "English": 88, "Science": 92},
    {"name": "Hari", "Math": 65, "English": 70, "Science": 60},
    {"name": "Gita", "Math": 78, "English": 82, "Science": 80},
    {"name": "Shyam", "Math": 55, "English": 60, "Science": 70}
]

# Calculate the total marks of a student
def calculate_total(student):
    subjects = ["Math", "English", "Science"]
    total = 0

    for subject in subjects:
        total += student[subject]

    return total

# Calculate the percentage of a student
def calculate_percentage(student):
    total = calculate_total(student)
    percentage = (total / 300) * 100
    return percentage

# Ask the user to enter a student name
student_name = input("Enter student name: ").strip()

try:
    # Find the student using their name
    student = next(
        s for s in students
        if s["name"].lower() == student_name.lower()
    )

    # Check whether all subject marks are available
    subjects = ["Math", "English", "Science"]
    for subject in subjects:
        if subject not in student:
            raise ValueError(f"{subject} marks are missing!")

    total = calculate_total(student)
    percentage = calculate_percentage(student)

    print("\nStudent Name:", student["name"])
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")

except StopIteration:
    print("Error: Student does not exist.")

except KeyError:
    print("Error: A subject mark is missing.")

except ValueError as error:
    print("Error:", error)

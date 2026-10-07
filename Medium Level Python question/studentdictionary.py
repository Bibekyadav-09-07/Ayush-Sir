student = {
    "name" : "Ram",
    "age" : 19,
    "course": "BCA",
    "marks":78
}

print("Student information:")
print(student)

#Increase marks by 5
student["marks"] = student["marks"] + 5

#Add status
if student["marks"] >= 40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"
print("\nUpdated student information:")
print(student)
    
marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}
print("Students and marks:")
for name, mark in marks.items():
    print(name,"-", mark)
print("Total marks:", sum(marks.values()))
print("Average marks:", sum(marks.values()) / len(marks))
print("Highest marks:", max(marks.values()))
print("Lowest marks:", min(marks.values()))
print("Name of the student with highest marks:", max(marks, key=marks.get))

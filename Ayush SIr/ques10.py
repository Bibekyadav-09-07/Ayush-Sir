marks = [75, 82, 68, 90, 55, 88,72, 95]
print("All marks:", marks)
total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_marks = max(marks)  
lowest_marks = min(marks)
print("Total marks:", total_marks)
print("Average marks:", average_marks) 
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)
count= 0
for mark in marks:
    if mark >= 75:
        count = count + 1
print("Students scoring 75 or more:", count)
marks.sort(reverse=True)
print("Marks from highest to lowest:", marks)
new_mark = int(input("Enter another student's mark: "))
marks.append(new_mark)
print("Updated marks:", marks)
print("Updated total marks:", sum(marks))
print("Updated average marks:", sum(marks) / len(marks))
print("Updated highest marks:", max(marks))
print("Updated lowest marks:", min(marks))
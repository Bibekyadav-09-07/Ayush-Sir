marks =[45, 78, 62, 89, 55, 92, 38, 76]

#Highest marks to lower marks
highest = max(marks)
lowest = min(marks)
#Average marks
average = sum(marks)/len(marks)
#count students above average
above_average = 0
for mark in marks:
    if mark > average:
        above_average += 1

        #sort marks
        ascending_marks = sorted(marks)
        print("Highest marks:", highest)
        print("Lowest marks:", lowest)  
        print("Average marks:", average)
        print("Students above average:", above_average)
        print("Marks in ascending order:", ascending_marks)
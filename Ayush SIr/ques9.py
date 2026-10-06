numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30 ]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print("Unique numbers:", unique_numbers)
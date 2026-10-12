
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

# Get student details
name = input("Enter student's name: ")

try:
    marks = float(input("Enter student's marks (0-100): "))

    if marks < 0 or marks > 100:
        print(Fore.RED + "Error: Marks must be between 0 and 100.")

    else:
        # Display the student's name in cyan
        print(Fore.CYAN + f"\nStudent Name: {name}")
        print(f"Marks: {marks:g}/100")

        # Check pass or fail
        if marks >= 40:
            print(Fore.GREEN + "Result: PASS")
        else:
            print(Fore.RED + "Result: FAIL")

except ValueError:
    print(Fore.RED + "Error: Please enter valid numeric marks.")

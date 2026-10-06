student ={
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"

}
key = input("Enter the key:")
if key in student:
    print(key, "exists in the dictionary.")
else:
    print(key, "does not exist in the dictionary.")
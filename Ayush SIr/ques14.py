book ={
    "title": "Python Basics",
    "author": "John Smith",
    "year":2025,
    "price": 500
}
print("All the keys:", book.keys())
print("All the values:", book.values())
print("All key-value pairs:", book.items())
for key, value in book.items():
    print(key, ":", value)
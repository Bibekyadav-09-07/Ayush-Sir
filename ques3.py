
books = [
    {"title": "Python Basics", "author": "Ram", "available": True},
    {"title": "Java Programming", "author": "Sita", "available": True},
    {"title": "Web Development", "author": "Hari", "available": True},
    {"title": "Database Systems", "author": "Gita", "available": False},
    {"title": "Computer Networks", "author": "Shyam", "available": True}
]

# Search for a book
def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book

    raise LookupError("Book does not exist.")

# Borrow a book
def borrow_book(title):
    book = search_book(title)

    if not book["available"]:
        print("Sorry, this book is already borrowed.")
    else:
        book["available"] = False
        print("You borrowed:", book["title"])

# Return a book
def return_book(title):
    book = search_book(title)

    if book["available"]:
        print("This book has not been borrowed.")
    else:
        book["available"] = True
        print("You returned:", book["title"])

# Display all available books
def display_available_books():
    print("\n----- AVAILABLE BOOKS -----")
    for book in books:
        if book["available"]:
            print(book["title"], "- Author:", book["author"])

# Main program
while True:
    print("\n1. Search Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "5":
        print("Thank you for using the library system.")
        break

    try:
        if choice in ["1", "2", "3"]:
            title = input("Enter book title: ").strip()

            if choice == "1":
                book = search_book(title)
                status = "Available" if book["available"] else "Borrowed"
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Status:", status)

            elif choice == "2":
                borrow_book(title)

            elif choice == "3":
                return_book(title)

        elif choice == "4":
            display_available_books()

        else:
            print("Invalid choice. Please select 1 to 5.")

    except LookupError as error:
        print("Error:", error)

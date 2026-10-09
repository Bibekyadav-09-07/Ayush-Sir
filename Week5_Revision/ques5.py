menu = {
    "momo": 150,
    "pizza": 350,
    "burger": 200,
    "chowmein": 180,
    "fried rice": 220,
    "sandwich": 160,
    "pasta": 280,
    "coffee": 100
}

order = []

# Display the menu
def display_menu():
    print("\n----- RESTAURANT MENU -----")
    for item, price in menu.items():
        print(item.title(), "- Rs.", price)

# Add an item to the order
def add_item(item, quantity):
    if item not in menu:
        raise KeyError("Food item is not on the menu.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    order.append({
        "item": item,
        "quantity": quantity,
        "price": menu[item]
    })

    print(item.title(), "added successfully.")

# Calculate the subtotal
def calculate_bill():
    subtotal = 0

    for entry in order:
        subtotal += entry["price"] * entry["quantity"]

    return subtotal

# Display the final order and bill
def display_order():
    print("\n----- FINAL ORDER -----")

    if not order:
        print("No items ordered.")
        return

    for entry in order:
        amount = entry["price"] * entry["quantity"]
        print(entry["item"].title(), "x", entry["quantity"],
              "= Rs.", amount)

    subtotal = calculate_bill()
    tax = subtotal * 0.13
    total = subtotal + tax

    print("\nSubtotal: Rs.", round(subtotal, 2))
    print("Tax (13%): Rs.", round(tax, 2))
    print("Final Bill: Rs.", round(total, 2))

# Main program
while True:
    display_menu()

    item = input("\nEnter food item or 'done': ").strip().lower()

    if item == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        add_item(item, quantity)

    except KeyError as error:
        print("Error:", error)

    except ValueError as error:
        print("Invalid quantity:", error)

# Print the final bill
display_order()

products = {
    "apple": {"price": 50, "quantity": 10},
    "milk": {"price": 80, "quantity": 5},
    "bread": {"price": 60, "quantity": 8},
    "rice": {"price": 100, "quantity": 10},
    "sugar": {"price": 90, "quantity": 6},
    "juice": {"price": 120, "quantity": 4}
}

cart = {}

# Add a product to the cart
def add_product(name, quantity):
    if name not in products:
        raise KeyError("Product does not exist.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    available = products[name]["quantity"]

    if quantity > available:
        raise ValueError(f"Only {available} items are available.")

    if name in cart:
        cart[name] += quantity
    else:
        cart[name] = quantity

    products[name]["quantity"] -= quantity
    print(name, "added to cart successfully.")

# Calculate the total price
def calculate_total():
    total = 0
    for name, quantity in cart.items():
        total += products[name]["price"] * quantity
    return total

# Display the cart
def display_cart():
    print("\n----- YOUR SHOPPING CART -----")
    if not cart:
        print("Your cart is empty.")
        return

    for name, quantity in cart.items():
        price = products[name]["price"]
        print(name, "x", quantity, "=", price * quantity)

    print("Total Price: Rs.", calculate_total())

# Allow multiple products to be added
while True:
    print("\nAvailable Products:")
    for name, details in products.items():
        print(name, "- Rs.", details["price"],
              "- Stock:", details["quantity"])

    name = input("\nEnter product name or 'done': ").strip().lower()

    if name == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        add_product(name, quantity)

    except KeyError as error:
        print("Error:", error)

    except ValueError as error:
        print("Invalid quantity or input:", error)

# Display the final bill
display_cart()

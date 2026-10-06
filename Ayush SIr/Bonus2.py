cart = ["apple", "banana", "apple", "mango"]

prices = {
    "apple": 100,
    "banana": 50,
    "mango": 150
}

total = 0

# Calculate total cost
for item in cart:
    total = total + prices[item]

print("Total =", total)
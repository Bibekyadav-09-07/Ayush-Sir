cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

#remove duplicates
cart = list(set(cart))

# Add cheese
cart.append("cheese")

# remove bread 
cart.remove("bread")

#Sort alphabetically
cart.sort()
print("Final cart:", cart)
print("Number of different items:", len(cart))
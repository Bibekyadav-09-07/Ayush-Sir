inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}
item = input("Enter item name: ").lower()
if item in inventory:
    sold = int(input("Enter quantity sold: "))
    if sold <= inventory[item]:
        inventory[item] = inventory[item] - sold

        #Remove item if quantity becomes 0
        if inventory[item] == 0:
            del inventory[item]
        print("Item sold successfully.")
    else:
        print("Not enough quantity available.")
else:
    print("Item not found.")
print("Updated inventory:")
print(inventory)
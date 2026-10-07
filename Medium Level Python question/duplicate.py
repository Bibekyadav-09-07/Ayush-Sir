names = ["Ram", "Sita", "Hari", "Ram", "Anu", "Sita", "Mina"]

# remove duplicates
unique_names = set(names)

# sort alphabetically
sorted_names = sorted(unique_names)
print("Unique names:", sorted_names)
print("Total number of unique students:", len(unique_names))
name = input("Enter your full name:")
# remove extra spaces
name = name.strip()

#convert to lowercase
name = name.lower()

#REPLACE SPACES WITH UNDERSCORE
username = name.replace(" ", "_")
print("Your username is:", username)